import logging

from app.base import tracker
from app import db
from flask import request, session
from app.base.models import VisitLog


def track_visitor():
    if not tracker.is_tracking_allowed():
        return
    else:
        ip_address = request.remote_addr
        requested_url = request.url
        referer_page = request.referrer
        page_name = request.path
        query_string = request.query_string
        user_agent = request.user_agent.string

        if tracker.track_session():

            log_id = session['log_id'] if 'log_id' in session else 0
            no_of_visits = session['no_of_visits']
            current_page = request.url
            previous_page = session['current_page'] if 'current_page' in session else ''

            print("track session")
            print(log_id)
            print(no_of_visits)
            print(f"prev {previous_page} / cur {current_page}")

            if previous_page != current_page:
                log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent, no_of_visits)
        else:
            session.modified = True
            print("track session false")

            try:
                log_id = log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent)

                # print('log_id', log_id)

                if log_id > 0:
                    next_visit = db.session.query(db.func.max(VisitLog.no_of_visits)).scalar()
                    if next_visit:
                        count = next_visit + 1
                    else:
                        count = 1

                    visit_log = VisitLog.query.filter_by(id=log_id).first()
                    visit_log.no_of_visits = count
                    db.session.commit()

                    session['track_session'] = True
                    session['no_of_visits'] = count
                    session['current_page'] = requested_url
                else:
                    session['track_session'] = False
            except Exception as e:
                db.session.rollback()
                logging.error(f"Track Session Exception : {str(e)}")
                session['track_session'] = False


def log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent, no_of_visits=None):
    visit_log = VisitLog()
    visit_log.ip_address = ip_address
    visit_log.requested_url = requested_url
    visit_log.referer_page = referer_page
    visit_log.page_name = page_name
    visit_log.query_string = query_string
    visit_log.user_agent = user_agent

    if no_of_visits is not None:
        visit_log.is_unique = False
        visit_log.no_of_visits = no_of_visits
    else:
        visit_log.is_unique = True
    try:

        db.session.add(visit_log)
        db.session.commit()
        log_id = visit_log.id
        return log_id
    except Exception as e:
        db.session.rollback()
        logging.error(f"Tracker DB Error : {str(e)}")


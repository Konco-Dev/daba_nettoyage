from flask import render_template, redirect, url_for, send_file, request,  jsonify
from app.base import blueprint
#from app.base.forms import SubscriptionForm
#from app import db
#from app.base.models import Subscriber
import logging
from app.base import visitor


@blueprint.route('/')
def route_default():
    return render_template("index.html", current_page="accueil")


@blueprint.route('/page_<error>')
def route_errors(error):
    return render_template('errors/page_{}.html'.format(error))


# @blueprint.before_request
# def track_request():
#     visitor.track_visitor()
#
#
# @blueprint.before_request
# def track_request():
#     visitor.track_visitor()


@blueprint.route('/logo')
def logo():
    return send_file("base/static/assets/img/logos/lit-logo-01.png")


# @blueprint.route('/subscribe', methods=['POST'])
# def subscribe():
#     subscriber_data = request.json
#
#     sub_form = SubscriptionForm(data=subscriber_data)
#     logging.info(f"Subscription POST : {request.remote_addr}")
#     if sub_form.validate():
#         try:
#             subscriber = Subscriber()
#             subscriber.fullname = sub_form.fullname.data
#             subscriber.email = sub_form.email.data
#             db.session.add(subscriber)
#             db.session.commit()
#             logging.info(f"New Subscription Added : {request.remote_addr}")
#         except Exception as e:
#             db.session.rollback()
#             logging.error(f"Subscription DB Error : {str(e)}")
#             return jsonify(status='error', msg=str(e)), 500
#         return jsonify(status='success'), 201
#
#     else:
#         logging.warning(f"Subscription Form Validation Error :"
#                         f"{request.remote_addr}/{sub_form.email.data}/{sub_form.fullname.data}")
#         return jsonify(staus='error', msg=sub_form.errors), 401


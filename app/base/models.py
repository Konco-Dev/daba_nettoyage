# # -*- encoding: utf-8 -*-
#
# from app import db
#
# class TimestampMixin(object):
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(
#         db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
#
#
# class Subscriber(db.Model, TimestampMixin):
#     __tablename__ = 'subscribers'
#
#     id = db.Column(db.Integer, primary_key=True)
#     fullname = db.Column(db.String(128), index=True)
#     email = db.Column(db.String(60), index=True)
#     is_subscribed = db.Column(db.Boolean, default=True)
#
#
# class VisitLog(db.Model):
#     __tablename__ = 'visits_log'
#
#     id = db.Column(db.Integer, primary_key=True)
#     no_of_visits = db.Column(db.Integer)
#     ip_address = db.Column(db.String(20))
#     requested_url = db.Column(db.Text)
#     referer_page = db.Column(db.Text)
#     page_name = db.Column(db.Text)
#     query_string = db.Column(db.Text)
#     user_agent = db.Column(db.Text)
#     is_unique = db.Column(db.Boolean, default=False)
#     access_date = db.Column(db.DateTime, server_default=db.func.now())
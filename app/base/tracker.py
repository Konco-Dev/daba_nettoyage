# from flask import request, session, current_app
#
#
# def is_tracking_allowed():
#     if current_app.config['DNT_TRACK']:
#         return True
#     if 'DNT' in request.headers and request.headers['DNT'] == 1:
#         return False
#     if request.remote_addr in current_app.config['IGNORE_IPS']:
#         return False
#     return True
#
#
# def track_session():
#     if 'track_session' in session and session['track_session'] is True:
#         return True
#     else:
#         return False
#
#

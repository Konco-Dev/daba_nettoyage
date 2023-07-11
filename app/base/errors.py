from app.base.tools import verify_pass
from flask import render_template, redirect, request, url_for, session

from app.base import blueprint


@blueprint.app_errorhandler(403)
def access_forbidden(error):
    return render_template('errors/page_403.html'), 403


@blueprint.app_errorhandler(400)
def request_error(error):
    return render_template('errors/page_400.html'), 400


@blueprint.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/page_404.html'), 404


@blueprint.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500

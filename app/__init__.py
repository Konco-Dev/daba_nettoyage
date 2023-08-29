# eventlet for deployment
#import eventlet
#eventlet.monkey_patch()
import os
from importlib import import_module
from logging import getLogger, Formatter, INFO
from logging.handlers import TimedRotatingFileHandler

from flask import Flask

from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy

from flask_wtf import CSRFProtect

import app
from flask_babel import Babel
from flask_moment import Moment


cors = CORS()
#db = SQLAlchemy()
csrf = CSRFProtect()

babel = Babel()
moment = Moment()


def register_extensions(app):
    #db.init_app(app)
    cors.init_app(app)
    csrf.init_app(app)
    babel.init_app(app)
    moment.init_app(app)


def register_blueprints(app):
    for module_name in ('base', 'admin', 'site'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


# def configure_database(app):
#     @app.teardown_request
#     def shutdown_session(exception=None):
#         #db.session.remove()


def configure_logs(app):
    try:
        if not os.path.isdir("logs"):
            os.makedirs("logs")

        if app.config["FILE_LOGS"]:
            logger = getLogger()
            rotation_handler = TimedRotatingFileHandler(filename='logs/runtime.log', utc=True, when='W0',
                                                        backupCount=15,
                                                        encoding='utf-8', delay=True)
            formatter = Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            rotation_handler.setFormatter(formatter)

            logger.addHandler(rotation_handler)
            logger.setLevel(INFO)
            logger.info('Konco Dev Logger startup')
    except:
        pass


def create_app(config, selenium=False):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)

    register_extensions(app)
    #configure_database(app)
    configure_logs(app)
    with app.app_context():
        register_blueprints(app)

    return app

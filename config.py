# -*- encoding: utf-8 -*-
import datetime
import os
from datetime import timedelta


class Config(object):

    HOST_URL = os.environ.get('HOST_URL')
    SERVER_NAME = os.environ.get('SERVER_NAME')

    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

    WTF_CSRF_TIME_LIMIT = None

    IGNORE_IPS = set([])

    LANGUAGES = ['en', 'fr', 'ar']
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

    # Launch date
    year = 2023
    month = 4
    day = 10
    hour = 0
    minute = 0
    second = 0

    launch_datetime = datetime.datetime(year, month, day, hour, minute, second)
    LAUNCH_DATE = launch_datetime


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DNT_TRACK = True
    FILE_LOGS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DNT_TRACK = False
    FILE_LOGS = True


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Development': DevelopmentConfig,
    'Debug': DebugConfig
}

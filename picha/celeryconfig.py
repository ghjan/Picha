# encoding: utf-8

# broker_url = 'pyamqp://'
# result_backend = 'rpc://'
# broker_url = 'redis://:DhG7n&5q@127.0.0.1:6379/7'
# result_backend = 'redis://:DhG7n&5q@127.0.0.1:6379/8'

# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# timezone = 'Asia/Shanghai'
# enable_utc = False


BROKER_URL = 'redis://:DhG7n&5q@127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://:DhG7n&5q@127.0.0.1:6379/2'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['application/json']  # ['json']

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = False

# djcelery 配置
# import djcelery
# djcelery.setup_loader()
# # BROKER_URL = 'redis://:DhG7n&5q@127.0.0.1:6379/1'
# BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
# CELERY_IGNORE_RESULT = True

# from celeryconfig_queue_simple import *
# from celeryconfig_queue_exchange_simple import *
# from celeryconfig_period import *

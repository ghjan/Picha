
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(process)d - [%(levelname)s] [%(asctime)s] - [%(pathname)s:%(lineno)d] - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'include_html': True,
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            # 'class': 'common.utils.log.AdminCeleryEmailHandler'
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'info_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/picha_info.log',
            'formatter': 'verbose',
        },
        'error_handler': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/picha_error.log',
            'formatter': 'verbose',
        },
        'task_info_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/picha_task.info.log',
            'formatter': 'verbose',
        },
        'task_error_handler': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/picha_task.error.log',
            'formatter': 'verbose',
        },
        'trace_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/picha_trace.log',
            'formatter': 'verbose',
        },

        'redis_info_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/picha_redis.info.log',
            'formatter': 'verbose',
        },
        'redis_error_handler': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/picha_redis.error.log',
            'formatter': 'verbose',
        },
        'cron_info_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/picha_cron.info.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['info_handler', 'error_handler'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.task': {
            'handlers': ['task_info_handler', 'task_error_handler'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.cron': {
            'handlers': ['cron_info_handler'],
            'level': 'INFO',
            'propagate': True,
        },
        'celery': {
            'handlers': ['task_info_handler', 'task_error_handler'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.redis': {
            'handlers': ['redis_info_handler', 'redis_error_handler'],
            'level': 'INFO',
            'propagate': True,
        },
        'trace': {
            'handlers': ['trace_handler'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

# # system default username
# SYSTEM_USER = 'system@fuwo.com'
# # system default message username
# SYSTEM_MESSAGE_USER = 'message@fuwo.com'
# # system default huxing username
# SYSTEM_HUXING_USER = 'huxing@fuwo.com'
#
# # system default model username
# SYSTEM_MODEL_USER = 'model@fuwo.com'

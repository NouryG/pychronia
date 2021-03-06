# -*- coding: utf-8 -*-
import logging.config


pychronia_logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'game_instance': {
            'format': '%(asctime)s [%(levelname)s] %(name)s[%(game_instance_id)s]: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'class':'logging.StreamHandler',
            'formatter': 'standard',
        },
        'game_instance': {
            'class':'logging.StreamHandler',
            'formatter': 'game_instance',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'pychronia_game': {
            'handlers': ['game_instance'],
            'level': 'INFO',
            'propagate': False
        },
        'django.db.backends': {
            'handlers': [],
            'level': 'WARNING',
            'propagate': False
        },
        'txn': { # ZODB transactions
            'handlers': [],
            'level': 'WARNING',
            'propagate': False
        },
        ## django.request is auto-configured to send admin emails when DEBUG=False ##
    }
}


logging.config.dictConfig(pychronia_logging_config)
logging.disable(logging.DEBUG) # global limit

# -*- coding: utf-8 -*-


from pychronia_game.common_settings import *

from pychronia_common.tests.transient_mode_settings import * # simple overrides

from pychronia_game.tests.common_test_settings import * # simple overrides


ROOT_URLCONF = 'pychronia_game.tests._test_urls_web'

ZODB_FILE = os.path.join(TEMP_DIR, 'gamedata.fs.%s' % UNICITY_STRING)
ZODB_URL = None

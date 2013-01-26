# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals


from .house_locking_mod import HouseLockingAbility
house_locking = HouseLockingAbility.as_view

from .runic_translation_mod import RunicTranslationAbility
runic_translation = RunicTranslationAbility.as_view

from .wiretapping_management_mod import WiretappingAbility
wiretapping_management = WiretappingAbility.as_view

from .mercenaries_hiring_mod import MercenariesHiringAbility
mercenaries_hiring = MercenariesHiringAbility.as_view

from .matter_analysis_mod import MatterAnalysisAbility
matter_analysis = MatterAnalysisAbility.as_view

from .world_scanning_mod import WorldScanAbility
world_scan = WorldScanAbility.as_view
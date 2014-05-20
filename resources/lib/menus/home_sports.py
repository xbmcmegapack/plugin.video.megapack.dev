#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    This file is part of XBMC Mega Pack Addon.

    Copyright (C) 2014 Wolverine (xbmcmegapack@gmail.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program.  If not, see http://www.gnu.org/licenses/gpl-3.0.html
"""

from home_sports_basketball import *
from home_sports_bowling import *
from home_sports_climbing import *
from home_sports_combat_sports import *
from home_sports_cue_sports import *
from home_sports_cycling import *
from home_sports_dart import *
from home_sports_equine_sports import *
from home_sports_fishing import *
from home_sports_football import *
from home_sports_golf import *
from home_sports_gymnastic import *
from home_sports_hockey import *
from home_sports_hunting import *
from home_sports_motor_racing import *
from home_sports_net_sports import *
from home_sports_poker import *
from home_sports_racket_sports import *
from home_sports_running import *
from home_sports_soccer import *
from home_sports_strength_sports import *
from home_sports_track_and_field import *
from home_sports_water_sports import *
from home_sports_winter_sports import *
from home_sports_xtreme_sports import *


class Sports():
    """Class that manages this specific menu context."""

    def open(self, plugin, menu):
        menu.add_folders(plugin.settings.get_sports())
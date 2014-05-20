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

from home_tvshows_animal import *
from home_tvshows_art import *
from home_tvshows_award import *
from home_tvshows_beauty import *
from home_tvshows_business import *
from home_tvshows_cars import *
from home_tvshows_celebrity import *
from home_tvshows_culture import *
from home_tvshows_economics import *
from home_tvshows_education import *
from home_tvshows_environment import *
from home_tvshows_fashion import *
from home_tvshows_food import *
from home_tvshows_gaming import *
from home_tvshows_gardening import *
from home_tvshows_health import *
from home_tvshows_history import *
from home_tvshows_house import *
from home_tvshows_lifestyle import *
from home_tvshows_news import *
from home_tvshows_outdoor import *
from home_tvshows_politics import *
from home_tvshows_realitytv import *
from home_tvshows_science import *
from home_tvshows_society import *
from home_tvshows_space import *
from home_tvshows_spirituality import *
from home_tvshows_superhero import *
from home_tvshows_technology import *
from home_tvshows_traveling import *
from home_tvshows_wildlife import *


class Tvshows():
    """Class that manages this specific menu context."""

    def open(self, plugin, menu):
        menu.add_folders(plugin.settings.get_topics())
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

from home_my_favourites import *
from home_my_playlist import *
from home_channels import *
from home_movies import *
from home_tvshows import *
from home_sports import *
from home_events import *
from home_live import *
from home_kids_zone import *
from home_languages import *
from home_countries import *
from home_adult import *
from home_search import *
from home_preferences import *


class Home():
    """Class that manages this specific menu context."""

    def open(self, plugin, menu):
        menu.add_folders(plugin.settings.get_home_menu(), False)
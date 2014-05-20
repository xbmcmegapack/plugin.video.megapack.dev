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

import xbmcaddon

from ..config import *


class Home_kids_zone():

    def make(self):
        """Generate Home_kids_zone menu file."""
        file = open(
            xbmcaddon.Addon().getAddonInfo('path') + PLUGIN_MENUS_FOLDER + \
                'home_kids_zone.py', 'w')
        file.write(PYTHON_HEADER + LICENCE)
        file.write("\n")
        file.write(\
"\
class Kids_zone():\n\
    \"\"\"Class that manages this specific menu context.\"\"\"\n\
\n\
    def open(self, plugin, menu):\n\
        menu.add_xplugins(plugin.get_xplugins(dictionaries=['All'],\n\
            genres=['Kids'], languages=['My'], countries=['My']))\
"
        )
        file.close()
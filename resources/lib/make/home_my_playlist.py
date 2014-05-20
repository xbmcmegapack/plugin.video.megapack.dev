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


class Home_my_playlist():

    def make(self):
        """Generate Home_my_playlist menu file."""
        file = open(
            xbmcaddon.Addon().getAddonInfo('path') + PLUGIN_MENUS_FOLDER + \
                'home_my_playlist.py', 'w')
        file.write(PYTHON_HEADER + LICENCE)
        file.write("\n")
        file.write(\
"\
\n\
import xbmcaddon\n\
import xbmcgui\n\
\n\
import config\n\
\n\
from ..data.keywords import KEYWORDS\n\
\n\
import dictionaries\n\
\n\
\n\
class My_playlist():\n\
\n\
\n\
    def show(self):\n\
    \"\"\"Class that manages this specific menu context.\"\"\"\n\
        xbmcgui.Dialog().ok(config.ADDON_NAME,\n\
            xbmcaddon.Addon().getLocalizedString(\n\
                dictionaries.Dictionaries().get_key(\n\
                    KEYWORDS, config.VARIA[0]) +\n\
                    '\n' + config.ADDON_WEB_SITE))\n\
"
        )
        file.close()
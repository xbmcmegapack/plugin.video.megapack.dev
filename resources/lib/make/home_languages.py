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

import codecs

import xbmcaddon

from ..config import *
from ..utils import _str


class Home_languages():

    def make(self):
        """ Generate Home_languages submenu files.
            Generate submenus first, so import in main menu file won't fail.
        """
        for language in (LANGUAGES_1 + LANGUAGES_2):
            name = _str.normalize(language)
            f = codecs.open(xbmcaddon.Addon().getAddonInfo('path') + \
                    PLUGIN_MENUS_FOLDER + 'home_languages_' + name.lower() + \
                    '.py', mode="w", encoding="utf-8-sig")
            f.write(PYTHON_HEADER + LICENCE + "\n")
            f.write(\
'\
class Languages_' + name.capitalize() + '():\n\
    \'\'\'Class that manages this specific menu context.\'\'\'\n\
\n\
    def open(self, plugin, menu):\n\
        menu.add_xplugins(plugin.get_xplugins(dictionaries=["Channels",\n\
            "Events", "Live", "Movies", "Sports", "TVShows"],\n\
            languages=["' + language.decode('utf-8') + '"]))\
'
            )
            f.close()
        """Generate Home_languages menu file."""
        file = open(
            xbmcaddon.Addon().getAddonInfo('path') + PLUGIN_MENUS_FOLDER + \
                'home_languages.py', 'w')
        file.write(PYTHON_HEADER + LICENCE)
        for language in (LANGUAGES_1 + LANGUAGES_2):
            file.write(\
"\
from home_languages_" + _str.normalize(language).lower() + " import *\n\
"
            )
        file.write("\n\n")
        file.write(\
"\
class Languages():\n\
    \"\"\"Class that manages this specific menu context.\"\"\"\n\
\n\
    def open(self, plugin, menu):\n\
        menu.add_folders(plugin.settings.get_languages())\
"
        )
        file.close()
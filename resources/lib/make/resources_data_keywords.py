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
from ...data.settings import *


class Resources_data_keywords():

    def make(self):
        """Generate resources/data/keywords.py"""
        f = codecs.open(
                xbmcaddon.Addon().getAddonInfo('path') + PLUGIN_KEYWORDS_FILE,\
                    mode="w", encoding="utf-8-sig")
        f.write(PYTHON_HEADER + LICENCE)
        f.write("# ID's are from /resources/language/English/string.xml\n")
        KEYWORDS = \
            SETTINGS_GENERAL + GENERAL + \
            SETTINGS_HOME + HOME + \
            SETTINGS_GENRES + GENRES + \
            SETTINGS_TOPICS + TOPICS + \
            SETTINGS_SPORTS + SPORTS + \
            SETTINGS_CHANNELS + CHANNELS + \
            SETTINGS_FEATURES + FEATURES + \
            SETTINGS_LANGUAGES + LANGUAGES_1 + \
            SETTINGS_LANGUAGES + LANGUAGES_2 + \
            SETTINGS_COUNTRIES + COUNTRIES_1 + \
            SETTINGS_COUNTRIES + COUNTRIES_2 + \
            SETTINGS_COUNTRIES + COUNTRIES_3 + \
            CONTEXT_MENU_FAVOURITES + \
            VARIA
        id = ADDON_I18N_START_ID
        f.write('KEYWORDS = \\\n')
        f.write('{\n')
        f.write('    "' + str(id) + '": "' + ADDON_NAME + '",\n')
        for keyword in KEYWORDS:
            id = id + 1
            f.write('    "' + str(id) + '": "' + keyword.decode('utf-8') + \
                        '",\n')
        f.write('}')
        f.close()
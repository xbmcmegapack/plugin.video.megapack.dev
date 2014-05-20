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


class Resources_lib_const():

    def make(self):
        """Generate resources/lib/const.py"""
        f = codecs.open(
                xbmcaddon.Addon().getAddonInfo('path') + PLUGIN_CONST_FILE,\
                    mode="w", encoding="utf-8-sig")
        f.write(PYTHON_HEADER + LICENCE + "\n")
        f.write("# ID's are from " + PLUGIN_LANGUAGE_ENGLISH_FOLDER + \
            PLUGIN_LANGUAGE_ENGLISH_FILE + "\n")
        # General
        #id = ADDON_I18N_START_ID + 3
        #f.write("GENERAL_MENU_FIRST_ID = " + str(id) + "\n")
        #id = id + len(GENERAL)
        #f.write("GENERAL_MENU_LAST_ID = " + str(id) + "\n")
        #id = id + 3
        id = ADDON_I18N_START_ID + 7
        f.write("HOME_MENU_FIRST_ID = " + str(id) + "\n")
        id = id + len(HOME) - 1
        f.write("HOME_MENU_LAST_ID = " + str(id) + "\n")
        id = id + 3
        f.write("GENRES_MENU_FIRST_ID = " + str(id) + "\n")
        id = id + len(GENRES) - 1
        f.write("GENRES_MENU_LAST_ID = " + str(id) + "\n")
        id = id + 3
        f.write("TOPICS_MENU_FIRST_ID = " + str(id) + "\n")
        id = id + len(TOPICS) - 1
        f.write("TOPICS_MENU_LAST_ID = " + str(id) + "\n")
        id = id + 3
        f.write("SPORTS_MENU_FIRST_ID = " + str(id) + "\n")
        id = id + len(SPORTS) - 1
        f.write("SPORTS_MENU_LAST_ID = " + str(id) + "\n")
        id = id + 3
        f.write("XCHANNELS_MENU_FIRST_ID = " + str(id) + "\n")
        id = id + len(CHANNELS) - 1
        f.write("XCHANNELS_MENU_LAST_ID = " + str(id) + "\n")
        id = id + 3
        f.write("FEATURES_MENU_FIRST_ID = " + str(id) + "\n")
        id = id + len(FEATURES) - 1
        f.write("FEATURES_MENU_LAST_ID = " + str(id) + "\n")
        id = id + 3
        f.write("LANGUAGES_MENU1_FIRST_ID = " + str(id) + "\n")
        id = id + len(LANGUAGES_1) - 1
        f.write("LANGUAGES_MENU1_LAST_ID = " + str(id) + "\n")
        id = id + 3
        f.write("LANGUAGES_MENU2_FIRST_ID = " + str(id) + "\n")
        id = id + len(LANGUAGES_2) - 1
        f.write("LANGUAGES_MENU2_LAST_ID = " + str(id) + "\n")
        id = id + 3
        f.write("COUNTRIES_MENU1_FIRST_ID = " + str(id) + "\n")
        id = id + len(COUNTRIES_1) - 1
        f.write("COUNTRIES_MENU1_LAST_ID = " + str(id) + "\n")
        id = id + 3
        f.write("COUNTRIES_MENU2_FIRST_ID = " + str(id) + "\n")
        id = id + len(COUNTRIES_2) - 1
        f.write("COUNTRIES_MENU2_LAST_ID = " + str(id) + "\n")
        id = id + 3
        f.write("COUNTRIES_MENU3_FIRST_ID = " + str(id) + "\n")
        id = id + len(COUNTRIES_3) - 1
        f.write("COUNTRIES_MENU3_LAST_ID = " + str(id) + "\n")
        id = id + 1
        f.write("CONTEXT_MENU_FAVOURITES_FIRST_ID = " + str(id) + "\n")
        id = id + len(CONTEXT_MENU_FAVOURITES) - 1
        f.write("CONTEXT_MENUS_FAVOURITES_LAST_ID = " + str(id))  # + "\n")
        #id = id + 1
        #f.write("VARIA_MENU_FIRST_ID = " + str(id) + "\n")
        #id = id + len(VARIA) - 1
        #f.write("VARIA_MENU_LAST_ID = " + str(id) + "\n")
        f.close()
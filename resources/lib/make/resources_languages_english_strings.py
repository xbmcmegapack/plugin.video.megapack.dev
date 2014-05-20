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


class Resources_languages_english_strings():

    def make(self):
        """Generate resources/language/English/string.xml"""
        f = codecs.open(
                xbmcaddon.Addon().getAddonInfo('path') + \
                PLUGIN_LANGUAGE_ENGLISH_FOLDER + 'strings.xml', mode="w",\
                encoding="utf-8-sig")
        f.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n')
        f.write('<!--\n' + LICENCE + '-->\n')
        f.write('<strings>\n')
        id = ADDON_I18N_START_ID
        f.write('    <string id="' + str(id) + '">' + \
                        ADDON_NAME.decode('utf-8') + '</string>\n')
        id = id + 1
        # General
        for string in (SETTINGS_GENERAL + GENERAL):
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Root Menu
        for string in (SETTINGS_HOME + HOME):
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Genres
        for string in (SETTINGS_GENRES + GENRES):
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Topics
        for string in (SETTINGS_TOPICS + TOPICS):
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Sports
        for string in (SETTINGS_SPORTS + SPORTS):
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Channels
        for string in (SETTINGS_CHANNELS + CHANNELS):
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Features
        for string in (SETTINGS_FEATURES + FEATURES):
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Languages (1)
        f.write('    <string id="' + str(id) + '">' + \
                    SETTINGS_LANGUAGES[0].decode('utf-8') + ' (1)</string>\n')
        id = id + 1
        f.write('    <string id="' + str(id) + '">' + \
                    SETTINGS_LANGUAGES[1].decode('utf-8') + '</string>\n')
        id = id + 1
        for string in LANGUAGES_1:
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Languages (2)
        f.write('    <string id="' + str(id) + '">' + \
                    SETTINGS_LANGUAGES[0].decode('utf-8') + ' (2)</string>\n')
        id = id + 1
        f.write('    <string id="' + str(id) + '">' + \
                    SETTINGS_LANGUAGES[1].decode('utf-8') + '</string>\n')
        id = id + 1
        for string in LANGUAGES_2:
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Countries (1)
        f.write('    <string id="' + str(id) + '">' + \
                    SETTINGS_COUNTRIES[0].decode('utf-8') + ' (1)</string>\n')
        id = id + 1
        f.write('    <string id="' + str(id) + '">' + \
                    SETTINGS_COUNTRIES[1].decode('utf-8') + '</string>\n')
        id = id + 1
        for string in COUNTRIES_1:
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Countries (2)
        f.write('    <string id="' + str(id) + '">' + \
                    SETTINGS_COUNTRIES[0].decode('utf-8') + ' (2)</string>\n')
        id = id + 1
        f.write('    <string id="' + str(id) + '">' + \
                    SETTINGS_COUNTRIES[1].decode('utf-8') + '</string>\n')
        id = id + 1
        for string in COUNTRIES_2:
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Countries (3)
        f.write('    <string id="' + str(id) + '">' + \
                    SETTINGS_COUNTRIES[0].decode('utf-8') + ' (3)</string>\n')
        id = id + 1
        f.write('    <string id="' + str(id) + '">' + \
                    SETTINGS_COUNTRIES[1].decode('utf-8') + '</string>\n')
        id = id + 1
        for string in COUNTRIES_3:
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        # Context menu.
        for string in CONTEXT_MENU_FAVOURITES:
            f.write('    <string id="' + str(id) + '">' + \
                        string.decode('utf-8') + '</string>\n')
            id = id + 1
        f.write('</strings>')
        f.close()
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


class Resources_settings():

    def make(self):
        """Generate resources/settings.xml"""
        f = codecs.open(
                xbmcaddon.Addon().getAddonInfo('path') + PLUGIN_SETTINGS_FILE,\
                    mode="w", encoding="utf-8-sig")
        f.write(XML_HEADER + '\n')
        f.write('<!--\n' + LICENCE + '-->\n')
        f.write('<settings>\n')
        id = ADDON_I18N_START_ID + 1
        # General
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_GENERAL[0].decode('utf-8') + '-->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="labelenum" default="720p" ' \
                'values="240p|360p|480p|720p|1080p|3D|4K" />\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="labelenum" default="5.1" ' \
                'values="1.0|2.0|5.1|7.1|9.1|11.1|10.2|22.2" />\n')
        f.write('    </category>\n')
        # Home menu
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_HOME[0].decode('utf-8') + '-->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in HOME:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="true" />\n')
        f.write('    </category>\n')
        # Genres
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_GENRES[0].decode('utf-8') + '-->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in GENRES:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="true" />\n')
        f.write('    </category>\n')
        # Topics
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_TOPICS[0].decode('utf-8') + '-->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in TOPICS:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="true" />\n')
        f.write('    </category>\n')
        # Sports
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_SPORTS[0].decode('utf-8') + '-->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in SPORTS:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="true" />\n')
        f.write('    </category>\n')
        # Channels
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_CHANNELS[0].decode('utf-8') + '-->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in CHANNELS:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="true" />\n')
        f.write('    </category>\n')
        # Features
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_FEATURES[0].decode('utf-8') + '-->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in FEATURES:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="true" />\n')
        f.write('    </category>\n')
        # Languages (1)
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_LANGUAGES[0].decode('utf-8') + ' (1) -->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in LANGUAGES_1:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="false" />\n')
        f.write('    </category>\n')
        # Languages (2)
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_LANGUAGES[0].decode('utf-8') + ' (2) -->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in LANGUAGES_2:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="false" />\n')
        f.write('    </category>\n')
        # Countries (1)
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_COUNTRIES[0].decode('utf-8') + ' (1) -->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in COUNTRIES_1:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="false" />\n')
        f.write('    </category>\n')
        # Countries (2)
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_COUNTRIES[0].decode('utf-8') + ' (2) -->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in COUNTRIES_2:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="false" />\n')
        f.write('    </category>\n')
        # Countries (3)
        id = id + 1
        f.write('    <category label="' + str(id) + '">' \
                '<!--' + SETTINGS_COUNTRIES[0].decode('utf-8') + ' (3) -->\n')
        id = id + 1
        f.write('        <setting id="' + str(id) + '" label="' + str(id) + \
                '" type="lsep" />\n')
        for menu_item in COUNTRIES_3:
            id = id + 1
            f.write('        <setting id="' + str(id) + '" ' \
                                'label="' + str(id) + '" type="bool" ' \
                                'default="false" />\n')
        f.write('    </category>\n')
        f.write('</settings>')
        f.close()
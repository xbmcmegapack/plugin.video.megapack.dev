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

import sys
import copy

import config

from _xbmc.addon import Xbmc_addon
from _xbmc.plugin import Xbmc_plugin
from _xbmc.gui import Xbmc_gui

from settings import Settings
from dictionaries import Dictionaries
from criteria import Criteria


class Plugin():
    """Mega Pack Plugin"""

    def __init__(self):
        """Private Properties."""
        self._xbmcaddon = Xbmc_addon()  # Facade and Decorator of xbmcaddon.
        self._xbmcplugin = Xbmc_plugin()  # Facade of xbmcplugin.
        self._xbmcgui = Xbmc_gui()  # Facade and Decorator of xbmcgui.
        self._handle = int(sys.argv[1])  # Plugin's id.
        self._path = self._xbmcaddon.getAddonInfo('path')  # Path of plugin in OS. Eg.: home/[usr]/.xbmc/addons/[plugin_name]
        self._url = str(sys.argv[0])  # Plugin's URL. Eg.: plugin://[plugin_name]
        self._nav = sys.argv[2].strip('?')  # Navigation route by user through plugin. Eg.: Movies_Action
        self._media_folder = self._path + config.PLUGIN_MEDIA_FOLDER  # Media folder path.
        self._dictionaries = Dictionaries()  # Dictionaries of this plugin.
        self._criteria = Criteria()  # Criteria filter class.
        """Public Properties."""
        self.settings = Settings()  # Settings of user for this plugin.

    """Implementation of IPlugin interface."""

    def run(self, menu):
        """Open requested menu by user."""
        if self._nav:
            menu.open(self._nav)  # Open requested menu by user.
        else:
            menu.open(config.PLUGIN_HOME)  # Startup menu (default).
        self._xbmcplugin.endOfDirectory(self._handle)

    def get_xplugins(self, dictionaries=[], genres=[], topics=[], sports=[],
                     features=[], languages=[], countries=[]):
        """Return a sleek dictionary as filter criteria."""
        dicts = self._dictionaries.get(dictionaries, \
                    'Adult' in self.settings.get_home_menu().values())
        xplugins = copy.deepcopy(dicts)
        delete_xplugin = True  # Flag to delete xplugins without any match.
        for name, xplugin in dicts.iteritems():
            for feed, meta in xplugin.iteritems():
                if isinstance(meta, dict):
                    if not self._criteria.evaluate(self.settings, meta,
                        genres, topics, sports, features, languages,
                        countries):  # TODO: or not self._settings.validate_general(meta):
                        del xplugins[name][feed]
                    else:
                        delete_xplugin = False
            if delete_xplugin:
                del xplugins[name]
            delete_xplugin = True
        return xplugins
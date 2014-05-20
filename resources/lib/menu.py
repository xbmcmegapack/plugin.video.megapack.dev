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

from ordereddict import OrderedDict

from ..data.keywords import KEYWORDS
from dictionaries import Dictionaries

import config

from utils import _str

from favourites_manager import *
from playlist_manager import *

from menus.home import *


class Menu():
    """Class that manages navigation of user through plugin' menus."""

    def __init__(self, plugin):
        """Private Properties."""
        self.xbmcaddon = plugin._xbmcaddon  # resources/lib/xbmc/addon.py
        self._xbmcplugin = plugin._xbmcplugin  # resources/lib/xbmc/plugin.py
        self._xbmcgui = plugin._xbmcgui  # resources/lib/xbmc/gui.py
        self._handle = plugin._handle
        self._path = plugin._path
        self._url = plugin._url
        self._nav = plugin._nav
        self._media_folder = plugin._media_folder
        self._plugin = plugin  # resources/lib/plugin.py

    """Implementation of IMenu interface."""

    def open(self, menu):
        exec menu + '().open(self._plugin, self)'

    """Implementation of IFolder interface."""

    def add_folders(self, folders, sorted_by_values=True):
        """Add many folders to a menu. Can be sorted by folder name."""
        translations = {}
        for id in folders:
            value = self.xbmcaddon.translate(id)
            translations.update({id: value})
        if sorted_by_values:  # Default.
            # IMPORTANT! This is the suggested way by Python 2.7, but it seems
            # to have problems when first letter is accented.
            translations = \
                OrderedDict(sorted(translations.items(), key=lambda t: t[1]))
            for id, folder in translations.iteritems():
                self._add_folder(id, folder, folders[id])
        else:  # Sorted by key.
            for id, folder in folders.iteritems():
                self._add_folder(id, translations[id], folder)

    """Implementation of IXPlugin interface."""

    def add_xplugins(self, xplugins, add_context_menu=True):
        """Add received xplugin feeds to calling menu."""
        for name, xplugin in xplugins.iteritems():
            for feed, meta in xplugin.iteritems():
                if isinstance(meta, dict):
                    ListItem = self._xbmcgui.ListItem(meta['label'], '', '',
                        self._make_thumb(xplugins[name]['name'],
                                         xplugins[name]['icon']))
                    # TODO: Find how to use Design Patterns to implement this
                    #       accordingly to callee' context: playable, folder...
                    if add_context_menu:
                        ListItem.addContextMenuItems(
                            self._make_favourites_context_menu(name, xplugin))
                    # IMPORTANT! isFolder MUST = True for external plugin
                    #            to work!
                    self._xbmcplugin.addDirectoryItem(self._handle,
                        meta['url'], ListItem, True)

    """Private methods."""

    def _add_folder(self, id, folder, name):
        """Add 1 folder to a menu."""
        ListItem = self._make_ListItem(id, folder, name)
        self._xbmcplugin.addDirectoryItem(
            self._handle, self._make_nav_url(name), ListItem, True)

    def _make_nav_url(self, name):
        """ Private method that returns the navigation query string of user.
            Query string uses seperator '_' to seperate levels of navigation.
            Eg.: Movies_Action
        """
        nav_url = self._url + '?' + self._nav
        if not self._nav:  # Home menu.
            nav_url += _str.normalize(name)
        else:
            nav_url += '_' + _str.normalize(name)
        return nav_url

    def _make_ListItem(self, id, item, icon):
        """Return a xbmcgui.ListItem."""
        icon_image = self._media_folder + icon + '.' + config.PLUGIN_ICON_EXT
        ListItem = self._xbmcgui.ListItem(item, '', icon_image)
        return ListItem

    def _make_thumb(self, name, icon):
        """Return a thumbnail for a xbmcgui.ListItem."""
        if name:  # A name is required for xplugin.
            return self._path.replace(config.PLUGIN_NAME, name) + icon
        else:  # For this plugin own icons library.
            return icon

    def _make_favourites_context_menu(self, name, xplugin):
        """Return favourites context menu."""
        favourites_context_menu = []
        favourites_context_menu.append(
            (self.xbmcaddon.translate(
                Dictionaries().get_key(KEYWORDS,
                config.CONTEXT_MENU_FAVOURITES[0])),\
                'XBMC.RunScript(' + config.ADDON_SPECIAL_PATH + \
                config.PLUGIN_NAME + config.PLUGIN_LIB + \
                'favourites_manager.py,' + \
                config.CONTEXT_MENU_FAVOURITES_COMMANDS[0] \
                + '(' + str({name: xplugin}) + '))'))
        favourites_context_menu.append(
            (self.xbmcaddon.translate(
                Dictionaries().get_key(KEYWORDS,
                config.CONTEXT_MENU_FAVOURITES[1])),\
                'XBMC.RunScript(' + config.ADDON_SPECIAL_PATH + \
                config.PLUGIN_NAME + config.PLUGIN_LIB + \
                'favourites_manager.py,' + \
                config.CONTEXT_MENU_FAVOURITES_COMMANDS[1] + \
                '("' + name + '"))'))
        favourites_context_menu.append(
            (self.xbmcaddon.translate(
                Dictionaries().get_key(KEYWORDS,
                config.CONTEXT_MENU_FAVOURITES[2])),\
                'XBMC.RunScript(' + config.ADDON_SPECIAL_PATH + \
                config.PLUGIN_NAME + config.PLUGIN_LIB + \
                'favourites_manager.py,' + \
                config.CONTEXT_MENU_FAVOURITES_COMMANDS[2] + ')'))

        return favourites_context_menu
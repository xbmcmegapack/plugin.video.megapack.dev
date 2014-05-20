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

# ORI from collections import OrderedDict
from ordereddict import OrderedDict

from _xbmc.addon import Xbmc_addon

import const

from ..data.keywords import KEYWORDS


class Settings():
    """Utilitary class for plugin' settings managment."""

    def __init__(self):
        """Private Properties."""
        self._xbmcaddon = Xbmc_addon()  # Facade and Decorator of xbmcaddon.

    """Implementation of IFeatures interface."""

    def get_favourites(self):
        """Return the list of user's favourites in plugin."""
        return []

    def get_playlist(self):
        """Return user's playlist."""
        return []

    def get_events(self):
        """Return events of the moment."""
        return []

    def get_live(self):
        """Return live shows of the moment."""
        return []

    """Implementation of IMegapackSettings interface."""

    # TODO: def validate_general(feed):

    #if len(general):  # TODO: REPLACE BY AUTOMATION, SINCE THIS IN SETTINGS.
    #    if general[0] == 'My':
    #        if not set(settings.get_general().values()) \
    #            .intersection(dictionary['general']):
    #            all_criteria_met = False
    #    else:
    #        if not set(dictionary['general']).intersection(general):
    #            all_criteria_met = False

    #def get_general(self):
    #    """Return a list of general settings selected in settings."""
    #    return self._get_tab(const.GENERAL_MENU_FIRST_ID,
    #                         const.GENERAL_MENU_LAST_ID)

    def get_home_menu(self):
        """Return a list of home menu items selected in settings."""
        return self._get_tab(const.HOME_MENU_FIRST_ID,
                             const.HOME_MENU_LAST_ID)

    def get_genres(self):
        """Return a list of genres selected in settings."""
        return self._get_tab(const.GENRES_MENU_FIRST_ID,
                             const.GENRES_MENU_LAST_ID)

    def get_topics(self):
        """Return a list of topics selected in settings."""
        return self._get_tab(const.TOPICS_MENU_FIRST_ID,
                             const.TOPICS_MENU_LAST_ID)

    def get_sports(self):
        """Return a list of sports selected in settings."""
        return self._get_tab(const.SPORTS_MENU_FIRST_ID,
                             const.SPORTS_MENU_LAST_ID)

    def get_xchannels(self):
        """Return a list of external channels selected in settings."""
        return self._get_tab(const.XCHANNELS_MENU_FIRST_ID,
                             const.XCHANNELS_MENU_LAST_ID)

    def get_features(self):
        """Return a list of features selected in settings."""
        return self._get_tab(const.FEATURES_MENU_FIRST_ID,
                             const.FEATURES_MENU_LAST_ID)

    def get_languages(self):
        """Return a list of languages selected in settings."""
        return self._get_tab(const.LANGUAGES_MENU1_FIRST_ID,
                             const.LANGUAGES_MENU2_LAST_ID)

    def get_countries(self):
        """Return a list of countries selected in settings."""
        return self._get_tab(const.COUNTRIES_MENU1_FIRST_ID,
                             const.COUNTRIES_MENU3_LAST_ID)

    """Private Methods."""

    def _get_tab(self, first_id, last_id):
        """Return a list of selected items in a tab section of settings."""
        selected_items = {}
        for id in range(first_id, last_id + 1):
            if self._xbmcaddon.getSetting(str(id)) == "true":
                selected_items.update({id: KEYWORDS[str(id)]})
        # Sort dictionary by key.
        selected_items = OrderedDict(sorted(selected_items.items()))
        return selected_items

    def _get_all(self, first_id, last_id):
        """Return a list of all items of a tab section' settings."""
        items = {}
        for id in range(first_id, last_id):
            items.update({id: KEYWORDS[str(id)]})
        return items
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

import copy

from ..data.xchannels import XChannels
from ..data.xmovies import XMovies
from ..data.xtvshows import XTVShows
from ..data.xsports import XSports
from ..data.xevents import XEvents
from ..data.xlive import XLive
from ..data.xkidszone import XKids_Zone
from ..data.xsearch import XSearch
from ..data.xadults import XAdults


class Dictionaries():
    """Utilitary class for plugin' dictionaries managment."""

    def get(self, names, adult=False):
        """Return a copy of asked dictionaries."""
        dictionaries = {}
        if names[0] == 'All':
            dictionaries = dict(XChannels.items() + XMovies.items() + \
                XTVShows.items() + XSports.items() + XEvents.items() + \
                XLive.items() + XKids_Zone.items())
            if adult:
                dictionaries = dict(dictionaries.items() + XAdults.items())
            return copy.deepcopy(dictionaries)
        if 'Channels' in names:
            dictionaries = XChannels
        if 'Movies' in names:
            dictionaries = dict(dictionaries.items() + XMovies.items())
        if 'TVShows' in names:
            dictionaries = dict(dictionaries.items() + XTVShows.items())
        if 'Sports' in names:
            dictionaries = dict(dictionaries.items() + XSports.items())
        if 'Events' in names and XEvents:  # Not empty.
            dictionaries = dict(dictionaries.items() + XEvents.items())
        if 'Live' in names and XLive:  # Not empty.
            dictionaries = dict(dictionaries.items() + XLive.items())
        if 'Kids_Zone' in names:
            dictionaries = dict(dictionaries.items() + XKids_Zone.items())
        if 'Search' in names:
            dictionaries = dict(dictionaries.items() + XSearch.items())
        if adult and 'Adult' in names:
            dictionaries = dict(dictionaries.items() + XAdults.items())
        return copy.deepcopy(dictionaries)

    def get_key(self, dictionary, value):
        """ Return the key according to value in dictionary.
            It is assumed that value is unique in dictonary.
            Internationalization is supported.
        """
        #ORI reverse_dict = {v: k for k, v in dictionary.items()}
        reverse_dict = {}
        for k, v in dictionary.items():
            reverse_dict.update({v: k})
        return int(reverse_dict[value])
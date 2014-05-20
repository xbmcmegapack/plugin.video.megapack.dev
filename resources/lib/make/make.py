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

from resources_data_keywords import Resources_data_keywords
from resources_lib_const import Resources_lib_const
from resources_settings import Resources_settings
from resources_languages_english_strings import \
    Resources_languages_english_strings
from home_my_favourites import Home_my_favourites
from home_my_playlist import Home_my_playlist
from home_channels import Home_channels
from home_movies import Home_movies
from home_tvshows import Home_tvshows
from home_sports import Home_sports
from home_events import Home_events
from home_live import Home_live
from home_kids_zone import Home_kids_zone
from home_countries import Home_countries
from home_languages import Home_languages
from home_adult import Home_adult
from home_search import Home_search
from home_preferences import Home_preferences
from home import Home


class Make():
    """ This class is used in the development phase only, it's not part of the
        final addon.
        It dynamically builts many files of this addon that do the same work,
        uppon different criteria.
    """

    def __init__(self):
        # Create main keywords dictionary file (English default).
        Resources_data_keywords().make()
        # Create const file.
        Resources_lib_const().make()
        # Create internationalization files (Default: English).
        Resources_settings().make()
        Resources_languages_english_strings().make()
        # Create menu classes tree from leafs to trunk.
        Home_my_favourites().make()
        Home_my_playlist().make()
        Home_channels().make()
        Home_movies().make()
        Home_tvshows().make()
        Home_sports().make()
        Home_events().make()
        Home_live().make()
        Home_kids_zone().make()
        Home_countries().make()
        Home_languages().make()
        Home_adult().make()
        Home_search().make()
        Home_preferences().make()
        Home().make()
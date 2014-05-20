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

from home_movies_action import *
from home_movies_adventure import *
from home_movies_animation import *
from home_movies_art_house_film import *
from home_movies_biography import *
from home_movies_christmas import *
from home_movies_classic import *
from home_movies_comedy import *
from home_movies_conspiration import *
from home_movies_crime import *
from home_movies_documentary import *
from home_movies_drama import *
from home_movies_family import *
from home_movies_fantastic import *
from home_movies_game import *
from home_movies_history import *
from home_movies_horror import *
from home_movies_independent import *
from home_movies_kids import *
from home_movies_mystery import *
from home_movies_music import *
from home_movies_musical import *
from home_movies_religion import *
from home_movies_romance import *
from home_movies_scifi import *
from home_movies_short_film import *
from home_movies_suspense import *
from home_movies_thriller import *
from home_movies_war import *
from home_movies_western import *


class Movies():
    """Class that manages this specific menu context."""

    def open(self, plugin, menu):
        menu.add_folders(plugin.settings.get_genres())
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

import os
import stat

import xbmcaddon

from ..config import *


class My_favourites():
    """Class that manages this specific menu context."""

    def __init__(self):
        """Private Properties."""
        f = xbmcaddon.Addon().getAddonInfo('path') + PLUGIN_MY_FAVOURITES_FILE
        self.dictionary = {}
        if not os.stat(f)[stat.ST_SIZE] == 0:  # If favourites file is not empty.
            self.dictionary = eval(open(f, 'r').read())

    def open(self, plugin, menu):
        menu.add_xplugins(self.dictionary)
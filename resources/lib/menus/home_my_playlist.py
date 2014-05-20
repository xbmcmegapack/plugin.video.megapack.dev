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

import xbmcaddon
import xbmcgui

from ..config import *

from ...data.keywords import KEYWORDS

from ..dictionaries import *


class My_playlist():
    """
    """

    def __init__(self):
        """
        """

    def open(self, plugin, menu):
        """
        """
        xbmcgui.Dialog().ok(ADDON_NAME,
            xbmcaddon.Addon().getLocalizedString(
                Dictionaries().get_key(
                    KEYWORDS, VARIA[0])) + '\n' + ADDON_WEB_SITE)
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

from ..config import *


class Home_my_favourites():

    def make(self):
        """Generate Home_my_favourites menu file."""
        file = open(
            xbmcaddon.Addon().getAddonInfo('path') + PLUGIN_MENUS_FOLDER + \
                'home_my_favourites.py', 'w')
        file.write(PYTHON_HEADER + LICENCE)
        file.write("\n")
        file.write(\
"\
\n\
import os\n\
import stat\n\
\n\
import xbmcaddon\n\
\n\
from ..config import *\n\
\n\
\n\
class My_favourites():\n\
    \"\"\"Class that manages this specific menu context.\"\"\"\n\
\n\
    def __init__(self):\n\
        \"\"\"Private Properties.\"\"\"\n\
        f = xbmcaddon.Addon().getAddonInfo('path') + PLUGIN_MY_FAVOURITES_FILE\n\
        self.dictionary = {}\n\
        if not os.stat(f)[stat.ST_SIZE] == 0:  # If favourites file is not empty.\n\
            self.dictionary = eval(open(f, 'r').read())\n\
\n\
    def open(self, plugin, menu):\n\
        menu.add_xplugins(self.dictionary)\
"
        )
        file.close()
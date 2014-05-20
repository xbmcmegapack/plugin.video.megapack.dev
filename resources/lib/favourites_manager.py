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
import sys
import copy

import xbmc

import config


class Favourites_manager():
    """ Class that manages this specific menu context."""

    def __init__(self):
        """Private Properties."""
        self.f = xbmc.translatePath(config.ADDON_SPECIAL_PATH) + \
            config.PLUGIN_NAME + config.PLUGIN_MY_FAVOURITES_FILE
        self.dictionary = {}
        if not os.stat(self.f)[stat.ST_SIZE] == 0:  # if not no favourites
            self.dictionary = copy.deepcopy(eval(open(self.f, 'r').read()))

    def add(self, favourite):
        """Add favourite to dictionary."""
        self.dictionary.update(favourite)
        f = open(self.f, 'w')
        f.write(str(self.dictionary))
        f.close()

    def delete(self, key):
        """Delete favourite from dictionary."""
        del self.dictionary[key]
        f = open(self.f, 'w')
        f.write(str(self.dictionary))
        f.close()

    def delete_all(self):
        """Delete all favourites from dictionary."""
        f = open(self.f, 'w')
        f.flush()
        f.close()

if __name__ == "__main__":
    context_menu_command = str(sys.argv[1])
    exec context_menu_command  # See config.CONTEXT_MENU_FAVOURITES_COMMANDS
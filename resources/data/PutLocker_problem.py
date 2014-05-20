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

XPlugins = \
{
    "PutlockerTV":
    {
        "label": "PutlockerTV",
        "name": "plugin.video.putlockertv",
        "icon": "/icon.png",
        "Tvshows_Realitytv":  # PROBLEM. THIS PLUGIN DO NOT CATEGORIZE ITS CONTENT, SO GROUPING IMPOSSILE IN MEGA PACK.
        {
            "label": "PutlockerTV: American Idol",
            "url": "plugin://plugin.video.putlockertv/?iconimage=http%3a%2f%2fwww.putlockertvshows.me%2fp%2famerican-idol.jpg&mode=902&name=American%20Idol&season=None&url=http%3a%2f%2fwww.putlockertvshows.me%2fwatch%2famerican-idol%2f",
            "general": [],
            "genres": [],
            "topics": ["Art","Celebrity","RealityTV"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
    },
}

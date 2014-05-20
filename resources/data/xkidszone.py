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


XKids_Zone = \
{
    "1-link movies":
    {
        "label": "1-link movies",
        "name": "plugin.video.1-linkmovies",
        "icon": "/icon.png",
        "Kids_zone":
        {
            "label": "1-link: Kids' Zone",
            "url": "plugin://plugin.video.1-linkmovies/?mode=GetTitles&numOfPages=1&section=ALL&startPage=1&url=http%3a%2f%2f1-linkmovies.com%2f%2fcategories%2fkidz-only-zone",
            "general": [],
            "genres": ["Family", "Kids"],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
    },
    "FullMovies":
    {
        "label": "FullMovies",
        "name": "plugin.video.fullmovies",
        "icon": "/icon.png",
        "Kids_zone":
        {
            "label": "FullMovies: Kids' Zone",
            "url": "plugin://plugin.video.fullmovies/?description&genre=Family&iconimage=%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.fullmovies%2ficon.png&mode=1&name=Family&url=http%3a%2f%2ffullmovies.cc%2fcategory-Family",
            "general": [],
            "genres": ["Family", "Kids"],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
    },
    "Hulu":
    {
        "label": "Hulu",
        "name": "plugin.video.hulu",
        "icon": "/icon.png",
        "Kids_zone":
        {
            "label": "Hulu: Kids' Zone",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d120%22",
            "general": [],
            "genres": ["Family", "Kids"],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
    },
    "Mash Up":
    {
        "label": "Mash Up",
        "name": "plugin.video.movie25",
        "icon": "/icon.png",
        "Kids_zone":
        {
            "label": "Mash Up: Kids' Zone",
            "url": "plugin://plugin.video.movie25/?fanart&genre&iconimage=https%3a%2f%2fraw.github.com%2fmash2k3%2fMashupArtwork%2fmaster%2fskins%2fgreenmonster%2fkidzone2.png&mode=76&name=Kids%20Zone&plot&url=http%3a%2f%2fwww.movie25.so%2f",
            "general": [],
            "genres": ["Family", "Kids"],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
    },
    "Movie25":  # HIGH ON MY LIST FOR NOW.
    {
        "label": "Movie25",
        "name": "plugin.video.moviestwentyfive",
        "icon": "/icon.png",
        "Kids_zone":
        {
            "label": "Movie25: Kids' Zone",
            "url": "plugin://plugin.video.movie25/?fanart&genre&iconimage=https%3a%2f%2fraw.github.com%2fmash2k3%2fMashupArtwork%2fmaster%2fskins%2fgreenmonster%2fkidzone2.png&mode=76&name=Kids%20Zone&plot&url=http%3a%2f%2fwww.movie25.so%2f",
            "general": [],
            "genres": ["Family", "Kids"],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
    },
    "Movie4K":
    {
        "label": "Movie4K",
        "name": "plugin.video.movie4k",
        "icon": "/icon.png",
        "Kids_zone":
        {
            "label": "Movie4K: Kids' Zone",
            "url": "plugin://plugin.video.movie4k/?action=movies_all&extra&page&plot&thumbnail&title=Family%20(3886%20movies)&url=http%3a%2f%2fwww.movie4k.to%2fmovies-genre-9-Family.html",
            "general": [],
            "genres": ["Family", "Kids"],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["Tonga", "United Kingdom", "United States"],
        },
    },
    "Much Movies HD":
    {
        "label": "Much Movies HD",
        "name": "plugin.video.muchmovies.hd",
        "icon": "/icon.png",
        "Kids_zone":
        {
            "label": "Much Movies HD: Kids' Zone",
            "url": "plugin://plugin.video.muchmovies.hd/?action=movies&url=http%3a%2f%2fwww.muchmovies.org%2fgenres%2ffamily%3fsort_by%3drelease",
            "general": [],
            "genres": ["Family", "Kids"],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
    },
    "PopcornFlix":
    {
        "label": "PopcornFlix",
        "name": "plugin.video.popcornflix",
        "icon": "/icon.png",
        "url": "plugin://plugin.video.popcornflix/",
        "Kids_zone":
        {
            "label": "PopcornFlix: Kids' Zone",
            "url": "plugin://plugin.video.popcornflix/?favtype=movies&mode=indexdeep&name=%5bCOLOR%20blue%5dKids%2fFamily%5b%2fCOLOR%5d&url=http%3a%2f%2fpopcornflix.com%2fFamily%2fKids-movies",
            "general": [],
            "genres": ["Family", "Kids"],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
    },
}

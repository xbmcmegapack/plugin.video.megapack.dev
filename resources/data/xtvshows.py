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

XTVShows = \
{
    "Hulu":  # THIS SITE HAS A STRUCTURE MORE OR LESS COMPATIBLE FOR
             # AGGREGATION, AND IT HAS A LOT OF PUBLICITIES, BUT GLOBAL
             # CONTENT AND QUALITY IS GOOD.
    {
        "label": "Hulu",
        "name": "plugin.video.hulu",
        "icon": "/icon.png",
        "Countries_Australia":
        {
            "label": "Hulu: Countries-Australia",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d161%22",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["Australia"],
        },
        "Countries_Canada":
        {
            "label": "Hulu: Countries-Canada",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d162%22",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["Canada"],
        },
        "Countries_China":
        {
            "label": "Hulu: Countries-China",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d162%22",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["Chinese","Mongolian","Tibetan", "Zhuang"],
            "countries": ["China"],
        },
        "Countries_India":
        {
            "label": "Hulu: Countries-India",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d137%22",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["Assamese", "Bengali", "English", "Gujarati",
                          "Hindi", "Kannada", "Kashmiri", "Malayalam",
                          "Marathi", "Nepali", "Oriya", "Sanskrit",
                          "Sindhi", "Tamil", "Telugu", "Urdu"],
            "countries": ["India"],
        },
        "Countries_Japan":
        {
            "label": "Hulu: Countries-Japan",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d136%22",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["Japanese"],
            "countries": ["Japan"],
        },
        "Countries_Korea":
        {
            "label": "Hulu: Countries-Korea",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d135%22",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["Korean"],
            "countries": ["Korea, Democratic People's Republic of", "Korea, Republic of"],
        },
        "Countries_Spain":
        {
            "label": "Hulu: Countries-Spain",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d111%22",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["Basque", "Catalan", "Galician", "Spanish"],
            "countries": ["Spain"],
        },
        "Countries_United_Kingdom":
        {
            "label": "Hulu: Countries-UK",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d138%22",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom"],
        },
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
        "Latino":
        {
            "label": "Hulu: Latino",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d111%22",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": [],
            "features": [],
            "languages": ["Aymara", "Haitian", "Portuguese", "Quechua", "Spanish"],
            "countries": ["Argentina", "Bolivia, Plurinational State of",
                          "Brazil", "Chile", "Colombia", "Costa Rica",
                          "Cuba", "Dominican Republic", "Ecuador",
                          "El Salvador", "Guatemala", "Haiti", "Honduras",
                          "Mexico", "Nicaragua", "Panama", "Paraguay",
                          "Puerto Rico", "Peru", "Uruguay",
                          "Venezuela, Bolivarian Republic of"],
        },
        "Sports_XTreme_Sports":
        {
            "label": "Hulu: Sports-XTreme",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d43%22",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": ["XTreme Sports"],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
        "Tvshows_Cars":
        {
            "label": "Hulu: TVShows-Cars-Bikes-Trucks",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d116%22",
            "general": [],
            "genres": [],
            "topics": ["Cars"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
        "Tvshows_Food":
        {
            "label": "Hulu: TVShows-Food",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d121%22",
            "general": [],
            "genres": [],
            "topics": ["Food"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
        "Tvshows_Health":
        {
            "label": "Hulu: TVShows-Health",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d66%22",
            "general": [],
            "genres": [],
            "topics": ["Health"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
        "Tvshows_Lifestyle":
        {
            "label": "Hulu: TVShows-Lifestyle",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d122%22",
            "general": [],
            "genres": [],
            "topics": ["Lifestyle"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
        "Tvshows_Music":
        {
            "label": "Hulu: TVShows-Music",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d9%22",
            "general": [],
            "genres": [],
            "topics": ["Music"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
        "Tvshows_Realitytv":
        {
            "label": "Hulu: TVShows-RealityTV",
            "url": "plugin://plugin.video.hulu/?art=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2fresources%2fimages%2ficon.png%22&fanart=%22%2fhome%2fjp%2f.xbmc%2faddons%2fplugin.video.hulu%2ffanart.jpg%22&mode=%22GridMenu%22&name=%22All%22&page=%221%22&popular=%22false%22&updatelisting=%22false%22&url=%22http%3a%2f%2fm.hulu.com%2fmenu%2f513340%3fchannel_id%3d11%22",
            "general": [],
            "genres": [],
            "topics": ["RealityTV"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
    },
    "Motor Sports (Replays)":
    {
        "label": "Motor Sports (Replays)",
        "name": "plugin.video.the666sicco",
        "icon": "/icon.png",
        "Sports_Motor_racing_f1_2013":
        {
            "label": "Motor Sports (Replays): F1 2013",
            "url": "plugin://plugin.video.the666sicco/?mode=browse&title=Formula1%202013&url=http%3a%2f%2fwww.666-sicco.info%2fformula2013.htm",
            "general": [],
            "genres": [],
            "topics": ["Cars"],
            "sports": ["Motor Racing"],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
        "Sports_Motor_racing_f1_2012":
        {
            "label": "Motor Sports (Replays): F1 2012",
            "url": "plugin://plugin.video.the666sicco/?mode=browse&title=Formula1%202012&url=http%3a%2f%2fwww.666-sicco.info%2fformula2012.htm",
            "general": [],
            "genres": [],
            "topics": ["Cars"],
            "sports": ["Motor Racing"],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
        "Sports_Motor_world_superbike_2014":
        {
            "label": "Motor Sports (Replays): World Superbike 2014",
            "url": "plugin://plugin.video.the666sicco/?mode=browse&title=World%20Superbike%202014&url=http%3a%2f%2fwww.666-sicco.info%2fsbk2014.htm",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": ["Motor Racing"],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
        "Sports_Motor_world_superbike_2013":
        {
            "label": "Motor Sports (Replays): World Superbike 2013",
            "url": "plugin://plugin.video.the666sicco/?mode=browse&title=World%20%20Superbike%202013&url=http%3a%2f%2fwww.666-sicco.info%2fsbk2013.htm",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": ["Motor Racing"],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
        "Sports_Motor_world_superbike_2012":
        {
            "label": "Motor Sports (Replays): World Superbike 2012",
            "url": "plugin://plugin.video.the666sicco/?mode=browse&title=World%20%20Superbike%202012&url=http%3a%2f%2fwww.666-sicco.info%2fsbk2012.htm",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": ["Motor Racing"],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
        "Sports_Motor_british_superbike_2013":
        {
            "label": "Motor Sports (Replays): British Superbike 2013",
            "url": "plugin://plugin.video.the666sicco/?mode=browse&title=British%20%20Superbike%202013&url=http%3a%2f%2fwww.666-sicco.info%2fbsb2013.htm",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": ["Motor Racing"],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
        "Sports_Motor_british_superbike_2012":
        {
            "label": "Motor Sports (Replays): British Superbike 2012",
            "url": "plugin://plugin.video.the666sicco/?mode=browse&title=British%20%20Superbike%202012&url=http%3a%2f%2fwww.666-sicco.info%2fbsb2012.htm",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": ["Motor Racing"],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
        "Sports_Motor_racing_motogp_2013":
        {
            "label": "Motor Sports (Replays): MotoGP 2013",
            "url": "plugin://plugin.video.the666sicco/?mode=browse&title=MotoGP%202013&url=http%3a%2f%2fwww.666-sicco.info%2fmotogp2013.htm",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": ["Motor Racing"],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
        "Sports_Motor_racing_motogp_2012":
        {
            "label": "Motor Sports (Replays): MotoGP 2012",
            "url": "plugin://plugin.video.the666sicco/?mode=browse&title=MotoGP%202012&url=http%3a%2f%2fwww.666-sicco.info%2fmotogp2012.htm",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": ["Motor Racing"],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
        "Sports_Motor_racing_motogp_2011":
        {
            "label": "Motor Sports (Replays): MotoGP 2011",
            "url": "plugin://plugin.video.the666sicco/?mode=browse&title=MotoGP%202011&url=http%3a%2f%2fwww.666-sicco.info%2fmotogp2011.htm",
            "general": [],
            "genres": [],
            "topics": [],
            "sports": ["Motor Racing"],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
    },
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
    "YouTube":
    {
        "label": "YouTube",
        "name": "plugin.video.youtube",
        "icon": "/icon.png",
        "Tvshows_Cars_yt_jay_leno_garage":
        {
            "label": "YouTube: Jay Leno's Garage",
            "url": "plugin://plugin.video.youtube/?feed=search&path=%2froot%2fsearch&search=Jay%20Leno%27s%20Garage",
            "general": [],
            "general": [],
            "genres": [],
            "topics": ["Cars"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
        "Tvshows_Cars_yt_motor_trend":
        {
            "label": "YouTube: Motor Trend",
            "url": "plugin://plugin.video.youtube/?feed=search&path=%2froot%2fsearch&search=Motor%20trend",
            "general": [],
            "genres": [],
            "topics": ["Cars"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
        "Tvshows_Cars_yt_top_gear":
        {
            "label": "YouTube: Top Gear",
            "url": "plugin://plugin.video.youtube/?feed=search&path=%2froot%2fsearch&search=top%20gear%20full%20episodesd",
            "general": [],
            "genres": [],
            "topics": ["Cars"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom", "United States"],
        },
        "Tvshows_Cars_yt_evo_magazine":
        {
            "label": "YouTube: Evo Magazine",
            "url": "plugin://plugin.video.youtube/?feed=search&path=%2froot%2fsearch&search=evo%20magazine",
            "general": [],
            "genres": [],
            "topics": ["Cars"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United Kingdom"],
        },
        "Tvshows_Cars_yt_the_fast_lane_car":
        {
            "label": "YouTube: The Fast Lane Car",
            "url": "plugin://plugin.video.youtube/?feed=search&path=%2froot%2fsearch&search=the%20fast%20lane%20car%20full%20episode",
            "general": [],
            "genres": [],
            "topics": ["Cars"],
            "sports": [],
            "features": [],
            "languages": ["English"],
            "countries": ["United States"],
        },
    },
}

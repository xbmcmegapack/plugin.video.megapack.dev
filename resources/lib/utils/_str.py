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


def normalize(input_str):
    """ Return a capitalized, without diacritic, string where space(s) have
        been replaced by underscore, and stripped of hyphens, apostrophes,
        parenthesis, commas and periods.
        Eg.: Movies >> Movies
             My Favourites >> My_favorites
             Virgin Islands, U.S. >> Virgin_islands_us
             Sint Maarten (Dutch Part) >> Sint_maarten_dutch_part
             Norvégien Bokmål >> Norvgien_bokml
    """
    return remove_diacritic(input_str.decode('utf-8')).lower(
        ).replace(' ', '_').replace('-', '').replace('(', '').replace(
        ')', '').replace(',', '').replace('.', '').replace(
        "'", '').capitalize()


def remove_diacritic(input_str):
    """ Remove accented characteres.
        From >> http://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
    """
    import unicodedata
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])
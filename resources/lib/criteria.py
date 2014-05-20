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


class Criteria():
    """Utilitary class for external plugins feeds criteria validations."""

    def evaluate(self, settings, dictionary, genres=[], topics=[], sports=[],
                 features=[], languages=[], countries=[]):
        """ Return True:
                - If all criteria are met in dictionary;
            Return False:
                - If a criteria is not met.
            NOTE: The 'My' value refers to all user's values for a setting.
                  Eg.: languages['My'] meens all user's languages selected
                       in settings.
            NOTE: A criteria is an enumeration to filter results.
                  Eg.: languages['English', 'French'] will return only feeds
                       in those languages.
        """
        all_criteria_met = True
        if len(genres):
            if genres[0] == 'My':
                if not set(settings.get_genres().values()) \
                    .intersection(dictionary['genres']):
                    all_criteria_met = False
            else:
                if not set(dictionary['genres']).intersection(genres):
                    all_criteria_met = False
        if len(topics):
            if topics[0] == 'My':
                if not set(settings.get_topics().values()) \
                    .intersection(dictionary['topics']):
                    all_criteria_met = False
            else:
                if not set(dictionary['topics']).intersection(topics):
                    all_criteria_met = False
        if len(sports):
            if sports[0] == 'My':
                if not set(settings.get_sports().values()) \
                    .intersection(dictionary['sports']):
                    all_criteria_met = False
            else:
                if not set(dictionary['sports']).intersection(sports):
                    all_criteria_met = False
        if len(features):
            if features[0] == 'My':
                if not set(settings.get_features().values()) \
                    .intersection(dictionary['features']):
                    all_criteria_met = False
            else:
                if not set(dictionary['features']).intersection(features):
                    all_criteria_met = False
        if len(languages):
            if languages[0] == 'My':
                if not set(settings.get_languages().values()) \
                    .intersection(dictionary['languages']):
                    all_criteria_met = False
            else:
                if not set(dictionary['languages']).intersection(languages):
                    all_criteria_met = False
        if len(countries):
            if countries[0] == 'My':
                if not set(settings.get_countries().values()) \
                    .intersection(dictionary['countries']):
                    all_criteria_met = False
            else:
                if not set(dictionary['countries']).intersection(countries):
                    all_criteria_met = False
        return all_criteria_met
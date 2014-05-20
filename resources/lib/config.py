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

"""CONFIGURATION OF THIS PLUGIN"""

XBMC = 'XBMC'

ADDON_NAME = 'Mega Pack'
ADDON_COPYRIGHT = '2014 Wolverine (xbmcmegapack@gmail.com)'
ADDON_WEB_SITE = 'http://www.megapack.com/'
ADDON_SPECIAL_PATH = 'special://home/addons/'

ADDON_I18N_START_ID = 30000  # Default by XBMC standard.
ADDON_I18N_MAX_ID = 30999  # Default by XBMC standard.

PLUGIN_NAME = 'plugin.video.megapack'
PLUGIN_VERSION = "0.0.1pa"
PLUGIN_LIB = "/resources/lib/"
PLUGIN_CONST_FILE = "/resources/lib/const.py"
PLUGIN_SETTINGS_FILE = "/resources/settings.xml"
PLUGIN_KEYWORDS_FILE = "/resources/data/keywords.py"
PLUGIN_MY_FAVOURITES = "My Favourites"
PLUGIN_MY_FAVOURITES_FILE = "/resources/lib/favourites.py"
PLUGIN_MY_FAVOURITES = "My Playlist"
PLUGIN_MY_PLAYLIST_FILE = "/resources/lib/playlist.py"
PLUGIN_HOME = 'Home'
PLUGIN_MEDIA_FOLDER = '/resources/media/'
PLUGIN_ICON_EXT = 'png'
PLUGIN_MENUS_FOLDER = '/resources/lib/menus/'
PLUGIN_LANGUAGE_ENGLISH_FOLDER = '/resources/language/English/'
PLUGIN_LANGUAGE_ENGLISH_FILE = 'strings.xml'

XML_HEADER = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>'

# File header declaration (used by resources/lib/make).
PYTHON_HEADER = "\
#!/usr/bin/python\n\
# -*- coding: utf-8 -*-\n\
"

# License declaration (used by resources/lib/make).
LICENCE = "\
\"\"\"\n\
    This file is part of " + XBMC + " " + ADDON_NAME + " Addon.\n\
\n\
    Copyright (C) " + ADDON_COPYRIGHT + "\n\
\n\
    This program is free software: you can redistribute it and/or modify\n\
    it under the terms of the GNU General Public License as published by\n\
    the Free Software Foundation, either version 3 of the License, or\n\
    (at your option) any later version.\n\
\n\
    This program is distributed in the hope that it will be useful,\n\
    but WITHOUT ANY WARRANTY; without even the implied warranty of\n\
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n\
    GNU General Public License for more details.\n\
\n\
    You should have received a copy of the GNU General Public License along\n\
    with this program.  If not, see http://www.gnu.org/licenses/gpl-3.0.html\n\
\"\"\"\n\n\
"

# Lists (used by resources/lib/make).

# Settings tabs.

GENERAL = ["Resolution", "Sound"]

# Settings tabs and plugin menus.

HOME = [\
    'My Favourites', 'My Playlist', 'Channels', 'Movies', 'TVShows', 'Sports',
    'Events', 'Live', "Kids' Zone", 'Languages', 'Countries', 'Adult',
    'Search', 'Preferences']
GENRES = [\
    "Action", "Adventure", "Animation", "Art House Film", "Biography",
    "Christmas", "Classic", "Comedy", "Conspiration", "Crime", "Documentary",
    "Drama", "Family", "Fantastic", "Game", "History", "Horror", "Independent",
    "Kids", "Mystery", "Music", "Musical", "Religion", "Romance", "Sci-Fi",
    "Short Film", "Suspense", "Thriller", "War", "Western"]
TOPICS = [\
    "Animal", "Art", "Award", "Beauty", "Business", "Cars", "Celebrity",
    "Culture", "Economics", "Education", "Environment", "Fashion", "Food",
    "Gaming", "Gardening", "Health", "History", "House", "Lifestyle", "News",
    "Outdoor", "Politics", "RealityTV", "Science", "Society", "Space",
    "Spirituality", "Superhero", "Technology", "Traveling", "Wildlife"]
SPORTS = [\
    "Basketball", "Bowling", "Climbing", "Combat Sports", "Cue Sports",
    "Cycling", "Dart", "Equine Sports", "Fishing", "Football", "Golf",
    "Gymnastic", "Hockey", "Hunting", "Motor Racing", "Net Sports", "Poker",
    "Racket Sports", "Running", "Soccer", "Strength Sports", "Track and Field",
    "Water Sports", "Winter Sports", "XTreme Sports"]
CHANNELS = [\
    "ARTE.TV", "DiY", "HGTV", "NASA", "BrewingTV", "Motor Sports Replays",
    "CBSNews", "Discovery News", "Discovery Channel", "Animal Planet", "TLC",
    "Science", "Destination America", "Investigation", "Military", "Velocity",
    "Fit and Health", "How Stuff Works", "ActionTV", "CBC TVShows",
    "CBC the Comedy Network", "America", "PutlockerTV", "RedBull.tv"]
FEATURES = [\
    "Livecams"]

# ALL BELLOW IS DIVIDED IN CHUNK OF 99 ITEMS BECAUSE TAB MAX ITEMS IS 100,
# AND FIRST ITEM OF A TAB IS A TEXT FOR USER.

LANGUAGES_1 = [\
    "Abkhazian", "Afar", "Afrikaans", "Akan", "Albanian", "Amharic", "Arabic",
    "Aragonese", "Armenian", "Assamese", "Avaric", "Avestan", "Aymara",
    "Azerbaijani", "Bambara", "Bashkir", "Basque", "Belarusian", "Bengali",
    "Bihari", "Bislama", "Bokmål", "Bosnian", "Breton", "Bulgarian", "Burmese",
    "Catalan", "Central Khmer", "Chamorro", "Chechen", "Chichewa", "Chinese",
    "Chuvash", "Cornish", "Corsican", "Cree", "Croatian", "Czech", "Danish",
    "Dutch", "Dzongkha", "English", "Esperanto", "Estonian", "Ewe", "Faroese",
    "Fijian", "Finnish", "French", "Fulah", "Gaelic", "Galician", "Ganda",
    "Georgian", "German", "Greek", "Guarani", "Gujarati", "Haitian", "Hausa",
    "Hebrew", "Herero", "Hindi", "Hiri Motu", "Hungarian", "Icelandic", "Ido",
    "Igbo", "Indonesian", "Interlingua", "Interlingue", "Inuktitut", "Inupiaq",
    "Irish", "Italian", "Japanese", "Javanese", "Kalaallisut", "Kannada",
    "Kanuri", "Kashmiri", "Kazakh", "Kikuyu", "Kinyarwanda", "Kirghiz", "Komi",
    "Kongo", "Korean", "Kuanyama", "Kurdish", "Lao", "Latin", "Latvian",
    "Limburgan", "Lingala", "Lithuanian", "Luba-Katanga", "Luxembourgish"]
LANGUAGES_2 = [\
    "Macedonian", "Malagasy", "Malay", "Malayalam", "Maldivian", "Maltese",
    "Manx", "Maori", "Marathi", "Marshallese", "Mongolian", "Nauru", "Navajo",
    "Ndonga", "Nepali", "North Ndebele", "Northern Sami", "Norwegian",
    "Norwegian", "Occitan", "Ojibwa", "Old Slavonic", "Oriya", "Oromo",
    "Ossetian", "Pali", "Panjabi", "Persian", "Polish", "Portuguese", "Pushto",
    "Quechua", "Romanian", "Romansh", "Rundi", "Russian", "Samoan", "Sango",
    "Sanskrit", "Sardinian", "Serbian", "Shona", "Sichuan Yi", "Sindhi",
    "Sinhala", "Slovak", "Slovenian", "Somali", "Sotho, Southern",
    "South Ndebele", "Spanish", "Sundanese", "Swahili", "Swati", "Swedish",
    "Tagalog", "Tahitian", "Tajik", "Tamil", "Tatar", "Telugu", "Thai",
    "Tibetan", "Tigrinya", "Tonga", "Tsonga", "Tswana", "Turkish", "Turkmen",
    "Twi", "Uighur", "Ukrainian", "Urdu", "Uzbek", "Venda", "Vietnamese",
    "Volapük", "Walloon", "Welsh", "Western Frisian", "Wolof", "Xhosa",
    "Yiddish", "Yoruba", "Zhuang", "Zulu"]
COUNTRIES_1 = [\
    "Afghanistan", "Åland Islands", "Albania", "Algeria", "American Samoa",
    "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda",
    "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan",
    "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia, Plurinational State of",
    "Bonaire, Sint Eustatius and Saba", "Bosnia and Herzegovina", "Botswana",
    "Bouvet Island", "Brazil", "British Indian Ocean Territory",
    "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia",
    "Cameroon", "Canada", "Cape Verde", "Cayman Islands",
    "Central African Republic", "Chad", "Chile", "China", "Christmas Island",
    "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo",
    "Congo, the Democratic Republic of the", "Cook Islands", "Costa Rica",
    "Côte d'Ivoire", "Croatia", "Cuba", "Curaçao", "Cyprus", "Czech Republic",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
    "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji",
    "Finland", "France", "French Guiana", "French Polynesia",
    "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany",
    "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe",
    "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti"]
COUNTRIES_2 = [\
    "Heard Island and McDonald Islands",
    "Holy See (Vatican City State)", "Honduras", "Hong Kong", "Hungary",
    "Iceland", "India", "Indonesia", "Iran, Islamic Republic of", "Iraq",
    "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey",
    "Jordan", "Kazakhstan", "Kenya", "Kiribati",
    "Korea, Democratic People's Republic of", "Korea, Republic of", "Kuwait",
    "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon",
    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
    "Macao", "Macedonia, the former Yugoslav Republic of", "Madagascar",
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico",
    "Micronesia, Federated States of", "Moldova, Republic of", "Monaco",
    "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar",
    "Namibia", "Nauru", "Nepal", "Netherlands", "New Caledonia", "New Zealand",
    "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island",
    "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau",
    "Palestine, State of", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar",
    "Réunion", "Romania", "Russian Federation", "Rwanda", "Saint Barthélemy",
    "Saint Helena, Ascension and Tristan da Cunha", "Saint Kitts and Nevis"]
COUNTRIES_3 = [\
    "Saint Lucia", "Saint Martin (French part)", "Saint Pierre and Miquelon",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino",
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
    "Sierra Leone", "Singapore", "Sint Maarten (Dutch part)", "Slovakia",
    "Slovenia", "Solomon Islands", "Somalia", "South Africa",
    "South Georgia and the South Sandwich Islands", "South Sudan", "Spain",
    "Sri Lanka", "Sudan", "Suriname", "Svalbard and Jan Mayen", "Swaziland",
    "Sweden", "Switzerland", "Syrian Arab Republic",
    "Taiwan, Province of China", "Tajikistan", "Tanzania, United Republic of",
    "Thailand", "Timor-Leste", "Togo", "Tokelau", "Tonga",
    "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
    "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States",
    "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu",
    "Venezuela, Bolivarian Republic of", "Viet Nam", "Virgin Islands, British",
    "Virgin Islands, U.S.", "Wallis and Futuna", "Western Sahara", "Yemen",
    "Zambia", "Zimbabwe"]

# IMPORTANT! These strings bellow are for internationalization. The addon
# code works with the english commands, but Dictionaries().get_key() will
# get the string in the user' language for user interface.

# Context menu Favourites options.

CONTEXT_MENU_FAVOURITES = [\
    "Add to " + ADDON_NAME + " Favourites",
    "Delete from " + ADDON_NAME + " Favourites",
    "Delete all " + ADDON_NAME + " Favourites"]

# Commands are for RunScript in Menu::_make_favourites_context_menu
CONTEXT_MENU_FAVOURITES_COMMANDS = [\
    "Favourites_manager().add",
    "Favourites_manager().delete",
    "Favourites_manager().delete_all()"]

# VARIA

VARIA = [\
    "To activate this feature please visit:"]
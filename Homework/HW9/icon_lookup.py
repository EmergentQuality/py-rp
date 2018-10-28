#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import emoji
# icon_dict = {'Mostly Cloudy': ':cloud:',
#              'Drizzle': '',
#              'Partly Sunny': ':partly_sunny:',
#              '\u1F325': 'sun behind large cloud',
#              '\u1F326': 'sun behind rain cloud',
#              '\u1F327': 'cloud with rain',
#              '\u1F328': 'cloud with snow',
#              '\u1F329': 'cloud with lightning',
#              '\u1F32A': 'tornado',
#              '\u1F32B': 'fog',
#              '0x2109': 'degrees Fahernheit',
#              '0xB0': 'degrees',
#             }

print(emoji.emojize("This is a cloud :cloud:", use_aliases=True))
print(emoji.emojize("\u2600"))
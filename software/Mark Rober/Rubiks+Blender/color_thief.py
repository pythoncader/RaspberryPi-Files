# -*- coding: utf-8 -*-

import sys

import io

from colorthief import ColorThief

color_thief = ColorThief("cube_cropped.jpg")
print(color_thief.get_color(quality=1))
print(color_thief.get_palette(quality=1))
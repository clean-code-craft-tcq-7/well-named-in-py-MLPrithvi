from Color_Constants import *

def generate_pair_number(major_color, minor_color):
  try:
    major_color_index = MajorColorNames.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_color_index = MinorColorNames.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_color_index * len(MinorColorNames) + minor_color_index + 1

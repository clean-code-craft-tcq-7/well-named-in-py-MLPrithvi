MAJOR_COLORS_LIST = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS_LIST = ["Blue", "Orange", "Green", "Brown", "Slate"]

def generate_pair_number(major_color, minor_color):
  try:
    major_color_index = MAJOR_COLORS_LIST.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_color_index = MINOR_COLORS_LIST.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_color_index * len(MINOR_COLORS_LIST) + minor_color_index + 1

def verify_pair_number(major_color, minor_color, expected_pair_number):
  pair_number = generate_pair_number(major_color, minor_color)
  assert(pair_number == expected_pair_number)

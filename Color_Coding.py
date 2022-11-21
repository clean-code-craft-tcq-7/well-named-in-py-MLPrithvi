MAJOR_COLORS_LIST = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS_LIST = ["Blue", "Orange", "Green", "Brown", "Slate"]

def generate_major_minor_color(pair_number):
  zero_based_pair_number = pair_number - 1
  major_color_index = zero_based_pair_number // len(MINOR_COLORS_LIST)
  if major_color_index >= len(MAJOR_COLORS_LIST):
    raise Exception('Major Color index out of range')
  minor_color_index = zero_based_pair_number % len(MINOR_COLORS_LIST)
  if minor_color_index >= len(MINOR_COLORS_LIST):
    raise Exception('Minor Color index out of range')
  return MAJOR_COLORS_LIST[major_color_index], MINOR_COLORS_LIST[minor_color_index]

def verify_major_minor_color(pair_number,
                            expected_major_color, expected_minor_color):
  major_color, minor_color = generate_major_minor_color(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)

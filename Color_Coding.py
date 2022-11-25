MajorColorNames = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MinorColorNames = ["Blue", "Orange", "Green", "Brown", "Slate"]

def generate_major_minor_color(pair_number):
  zero_based_pair_number = pair_number - 1
  major_color_index = zero_based_pair_number // len(MinorColorNames)
  if major_color_index >= len(MajorColorNames):
    raise Exception('Major Color index out of range')
  minor_color_index = zero_based_pair_number % len(MinorColorNames)
  if minor_color_index >= len(MinorColorNames):
    raise Exception('Minor Color index out of range')
  return MajorColorNames[major_color_index], MinorColorNames[minor_color_index]

def verify_major_minor_color(pair_number,
                            expected_major_color, expected_minor_color):
  major_color, minor_color = generate_major_minor_color(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)

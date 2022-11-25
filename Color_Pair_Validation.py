from Color_Coding import generate_major_minor_color
from Number_Coding import generate_pair_number

def verify_major_minor_color(pair_number,
                            expected_major_color, expected_minor_color):
  major_color, minor_color = generate_major_minor_color(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)
  
def verify_pair_number(major_color, minor_color, expected_pair_number):
  pair_number = generate_pair_number(major_color, minor_color)
  assert(pair_number == expected_pair_number)
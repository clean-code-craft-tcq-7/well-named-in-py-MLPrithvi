from Pair_Color_Code_Menu import *
from Color_Pair_Validation import *

if __name__ == '__main__':
  verify_major_minor_color(4, 'White', 'Brown')
  verify_major_minor_color(5, 'White', 'Slate')
  verify_pair_number('Black', 'Orange', 12)
  verify_pair_number('Violet', 'Slate', 25)
  verify_pair_number('Red', 'Orange', 7)
  print_pair_color_code_menu(1,25)

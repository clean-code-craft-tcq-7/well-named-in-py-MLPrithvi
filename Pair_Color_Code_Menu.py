from Color_Coding import *
from Number_Coding import *

print("Pair Number = Major Color + Minor Color")
print("=======================================")

def print_pair_color_code_menu(min_number,max_number):
    for pair_number in range(min_number,max_number+1):
        zero_based_pair_number = pair_number - 1
        major_color_index = zero_based_pair_number // len(MINOR_COLORS_LIST)
        minor_color_index = zero_based_pair_number % len(MINOR_COLORS_LIST)
        major_color = MAJOR_COLORS_LIST[major_color_index]
        minor_color = MINOR_COLORS_LIST[minor_color_index]
        print(f'{pair_number} = {major_color} + {minor_color}')
        print("---------------------")
    return(f'{pair_number} = {major_color} + {minor_color}')

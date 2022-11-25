from Color_Coding import *

print("Pair Number = Major Color + Minor Color")
print("=======================================")

def print_pair_color_code_menu(min_number,max_number):
    for pair_number in range(min_number,max_number+1):
        major_color, minor_color = generate_major_minor_color(pair_number)
        print(f'{pair_number} = {major_color} + {minor_color}')
        print("---------------------")
    return(f'{pair_number} = {major_color} + {minor_color}')

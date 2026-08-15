###############################################

#import math_utils

#print(math_utils.add(10, 5))
#print(math_utils.subtract(10, 5))
#print(math_utils.multiply(10, 5))
#print(math_utils.divide(10, 5))

###############################################

#from math_utils import add, subtract

#print(add(10, 5))
#print(subtract(10, 5))

###############################################

#import math_utils as math

#print(math.add(5, 3))

###############################################

import math_utils
import string_utils
from math_utils import add, subtract   # allow use of Add and Subtract functions without any prefix

def main():
    name = input("Enter your name: ")

    clean_name = string_utils.normalize_name(name)

    string_utils.display_title("Developer Profile")

    print(f"Name: {clean_name}")
    print(f"5 * 3 = {math_utils.multiply(5, 3)}")  # using the multiply function in the imported module
    print(f"5 + 3 = {add(5, 3)}")  #Using the imported Add function directly
    print(f"5 - 3 = {subtract(5, 3)}")  #Using the imported Subtract function directly

if __name__ == "__main__":  # Run this block only when this file is executed directly, not when it is imported.
    main()

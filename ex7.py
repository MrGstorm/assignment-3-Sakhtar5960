###############################################################################
#  Program Name   : ex7
#  Author         : Hamza Akhtar
#  Task           : Checks which number is greater based on the 2 numbers you provide 
###############################################################################
# ----------------------------------------------------------------
number1 = int(input('Choose a number: '))                       # |
number2 = int(input('Choose a number: '))                       # |
                                                                # |
if number1 > number2:                                           # |
    print(number1, 'is greater than', number2)                  # |
if number1 < number2:                                           # |
    print(number1, 'is less than', number2)                     # |
elif number1 == number2:                                        # |
    print('These numbers are the same.')                        # |
# -----------------------------------------------------------------
###############################################################################
#  Program Name   : ex10
#  Author         : Hamza Akhtar
#  Task           : Asks you for your friends names and returns a list. 
###############################################################################
# Asks for friends names
friend1  = input('Enter the name of the a friend (1/3): ')
friend2  = input('Enter the name of the a friend (2/3): ')
friend3  = input('Enter the name of the a friend (3/3): ')
# Creates list
friend_list = [friend1, friend2, friend3]
# Prints the list
for item in friend_list:
    print(item)
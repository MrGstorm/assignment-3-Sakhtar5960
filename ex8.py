###############################################################################
#  Program Name   : ex8
#  Author         : Hamza Akhtar
#  Task           : Asks you for random words until you quit.
###############################################################################
print('Enter STOP to quit. ')
while True:
    x = input('Type a random word: ')
    if x == 'STOP':
        print('Quitting program')
        break
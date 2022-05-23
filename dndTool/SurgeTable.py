import pandas as pd
import random

def printFull(indexSurge, df):
    Effect = df.iloc[indexSurge]['Effect']
    Intensity = str(df.iloc[indexSurge]['Intensity'])

    print('Rolled: ' + str(indexSurge + 1))
    print('Effect: ' + Effect)
    print('Intensity: ' + Intensity)

print('################################')
print('WELCOME TO BRI\'S SURGE TABLE')
print('################################')
print('This table is designed to replace the traditional PHB Wild Magic Surge Table, and has real consequences to the world.')
print('The program however, allows you to roll on the table, or index the specific one if you had already rolled..')
print('Or even roll using the specific intensity modifiers!')
print('Version 0.95')

df = pd.read_excel('wild_magic.xlsx') # Yes, you do need to have a file named "wild_magix.xlsx" in the fucking directory.
quit = False

userIn = input('\n\t\t\tReady to Roll on the Table? \n\t Index a Number, Enter, or Define the Intensity or q to quit. \n')
if userIn == 'q': quit = True
intensityLevel = ['mid', 'weak', 'extreme'] # As far as I know, this is all the possible intensity levels. You can probably update just the list, and it'll still work.

while quit is False: # This is the loop, instantiated above.
    usedDataframe = df 
    indexSurge = 0

    if userIn.isnumeric() and int(userIn) in range(0, len(df)): # Checks if the input is numeric and between 0 - 414.
        indexSurge = int(userIn) - 1
    elif userIn.lower() in intensityLevel: # Checks if the input is in the intensityLevel List.
        usedDataframe = df[df.Intensity == userIn]
        indexSurge = random.randint(0, len(usedDataframe))
    else: # Any other input which would have been recognized as invalid, will instead return a random.
        indexSurge = random.randint(0, len(df))

    printFull(indexSurge, usedDataframe)

    userIn = input('\n\t\t\tReady to Roll on the Table? \n\t Index a Number, Enter, or Define the Intensity or q to quit. \n')
    if userIn == 'q': quit = True

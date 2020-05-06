# Calculates miles per gallon to kilometers per liter
#MonceRomero_03_01_02

mil_per_gal = int(input("Enter a figure for miles per gallon. "))

if mil_per_gal == 0 or mil_per_gal == '':
    exit()

#Calculations for converting miles/gallon into kilo/liter
kilometers = mil_per_gal * 1.61
kilo_per_liter = round(kilometers / 3.79, 1)
print("This is your input for miles per gallon: ", mil_per_gal)
print("This is the output for kilometers per liter: ", kilo_per_liter)

exit() #End of program

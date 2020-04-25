# It will convert the height from feet and inches into meters
#MonceRomero_03_01_01

print("Enter a number to be converted into meters.")
feet_value = input("Enter value for feet. ")
inch_value = input("Enter value for inches. ")

if feet_value == '':
    exit()

if inch_value == '':
    exit()

feet_value = int(feet_value)
inch_value = int(inch_value)

# Total amount of inches
total_inches = inch_value + int((feet_value*12))
print("The total inches is: ", total_inches)

if total_inches >= 96:
    print("This person is really tall!")

total_centi = total_inches * 2.54
meters = round(total_centi / 100, 2)

print("The orginal height is", feet_value, "feet and",
      inch_value, " inches.")
print("The equivalence in meters is ", meters)

exit() #End of program

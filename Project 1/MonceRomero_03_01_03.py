# Prints the colors of a square from a chessboard
#MonceRomero_03_01_03

print("This program will print the color of a square from a chessboard\n"
      "Your input should be in the form of a letter and a number\n"
      "For example: the input should be a1\n"
      "One letter and one number will be fine, please and thank you")

user_input = input("Enter your input: ")
print("Your input is: ",user_input)

first_char  = ord(user_input[0])
second_char = int(user_input[1])

if first_char not in range(97,105):
    print("Your letter is not within the range of a-h")
    exit()

if second_char not in range(1,9):
    print("Your number is not within the range of 1-8")
    exit()

if second_char % 2 == 0 and first_char % 2 == 1:
    print("Square", user_input, "is white")
elif second_char % 2 == 1 and first_char % 2 == 0:
    print("Square", user_input, "is white")
elif second_char % 2 == 0 and first_char % 2 == 0:
    print("Square", user_input, "is black")
elif second_char % 2 == 1 and first_char % 2 == 1:
    print("Square", user_input, "is black")

exit()

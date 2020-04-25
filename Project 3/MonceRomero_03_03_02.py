# Program that uses Python's list comprehension
# Program will take numbers from the user and it calculate
# the average and it will output the numbers that are below, equal and above the average

def main():
    print("Enter a few numbers and I will calculate\n"
          "the below and above average. Press 0 to stop")
    user_input = '*'
    num = []

    while user_input != 0:
        user_input = float(input("Enter a number: "))
        if user_input == 0:
            break
        num.append(user_input)

    total = 0
    if len(num) == 0:
        print("Division by '0' error!")
        quit()

    for number in num:
        total += number

    average = float(total / len(num))
    below_ave = []
    equal_ave = []
    above_ave = []

    for number in num:
        if number < average:
            below_ave.append(number)
        elif number == average:
            equal_ave.append(number)
        elif number > average:
            above_ave.append(number)

    print("The average is:" ,average)
    print("Numbers in your list that are below the average:" ,below_ave)
    print("Numbers in your list that are equal to the average:" ,equal_ave)
    print("Numbers in your list that are above the average:" ,above_ave)


if __name__ == "__main__":
    main()

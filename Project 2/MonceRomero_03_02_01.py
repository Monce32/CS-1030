

def main():
    print("Enter your grades and I will calculate your GPA")
    print("Enter 'quit' to stop the program or press 'enter' to\n"
          "to calculate your grade")

    response = True
    total_points = 0
    total_grades = 0
    my_overall_score = []
    grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
    my_response = "*"

    while response:
        while my_response != '':
            my_response = input("Enter a grade: ")
            if my_response == "quit":
                response = False
            elif my_response not in grades:
                if my_response == '':
                    break
                print("Please try again")
                continue
            grade_point = calc_grade(my_response)
            total_points += grade_point
            total_grades += 1

        if my_response == '' and total_grades == 0:
            print("No grade was calculated")
            my_response = input("Do you want to continue? Enter 'yes' or 'no'. ")
            if my_response == 'no':
                response = False
            else:
                continue

        elif my_response == '':
            print("Your current GPA is:", round(total_points / total_grades, 2))
            my_overall_score.append(round(total_points / total_grades, 2))
            total_points = 0
            total_grades = 0
            my_response = input("Do you want to continue? Enter 'yes' or 'no'. ")
            if my_response == 'no':
                response = False
            else:
                continue

    print("Your overall average is:",round(overall_grade(my_overall_score), 2))

def overall_grade(total):
    overall_score = 0

    for grade in total:
        overall_score += grade

    return overall_score / len(total)

def calc_grade(my_response):

    if my_response == 'A+':
        return 4.2
    elif my_response == 'A':
        return 4
    elif my_response == 'A-':
        return 3.9
    elif my_response == 'B+':
        return 3.7
    elif my_response == 'B':
        return 3.2
    elif my_response == 'B-':
        return 3.0
    elif my_response == 'C+':
        return 2.8
    elif my_response == 'C':
        return 2.2
    elif my_response == 'C-':
        return 2.0
    elif my_response == 'D+':
        return 1.8
    elif my_response == 'D':
        return 1.2
    else:
        return 0


if __name__ == '__main__':
    main()

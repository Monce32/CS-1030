# Program that uses a dictionary and asks for a canadian postal code
# Once the user enters a postal code it will validate it

def main():
    table = {'A': 'Newfoundland',
             'B': 'Nova Scotia',
             'C': 'Prince Edward Island',
             'E': 'New Brunswick',
             'G': 'Quebec',
             'H': 'Quebec',
             'J': 'Quebec',
             'K': 'Ontario',
             'L': 'Ontario',
             'M': 'Ontario',
             'N': 'Ontario',
             'P': 'Ontario',
             'R': 'Manitoba',
             'S': 'Saskatchewan',
             'T': 'Alberta',
             'V': 'British Columbia',
             'X': ['Nunavut', 'Northwest Territories'],
             'Y': 'Yukon'}

    print("Enter a valid postal code and once you are done\n"
          "entering a postal press 'Enter'.")

    postal_code = []
    user_input = '*'
    while user_input != '':
        user_input = input("Enter your postal code: ")
        if user_input == '':
            print("End of input")
            break
        print("Your postal code is:" ,validation(user_input, table))
        if validation(user_input, table) == 'Not valid':
            continue
        elif validation(user_input, table) == 'Valid':
            postal_code.append(user_input)

    for single_postal in postal_code:
        if single_postal[1] == '0':
            address = 'rural'
        else:
            address = 'urban'
        print("Your address is a " + address + " one in" ,table[single_postal[0]] )

# Validates the postal code
def validation(postal, table):

    if len(postal) != 7:
        return 'Not Valid'

    if postal[4] == ' ':
        return 'Not Valid'

    if postal[0] not in table:
        return 'Not Valid'

    return 'Valid'

if __name__ == "__main__":
    main()

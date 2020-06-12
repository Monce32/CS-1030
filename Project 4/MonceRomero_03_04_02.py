# Opens a file and determines the frequency of each letter

def main():
    letters = {'A': 0, 'B': 0,  'C': 0,
               'D': 0, 'E': 0,  'F': 0,
               'G': 0, 'H': 0,  'I': 0,
               'J': 0, 'K': 0,  'L': 0,
               'M': 0, 'N': 0,  'O': 0,
               'P': 0, 'Q': 0,  'R': 0,
               'S': 0, 'T': 0,  'U': 0,
               'V': 0, 'W': 0,  'X': 0,
               'Y': 0, 'Z': 0}

    with open('1030 Project 04 02 Sentences.txt') as file_object:
        contents = file_object.readlines()
        for line in contents:
            my_line = line.rstrip()
            print(my_line)
            upper_line = my_line.upper()
            for each_letter in upper_line:
                if each_letter.isalpha():
                    letters[each_letter] += 1

    file_object.close()

    filename = 'MonceRomero 03 04 02 Output.txt'
    with open(filename, 'w') as new_file:
        print("Letter    Frequency")
        new_file.write("Letter    Frequency")
        for letter in letters:
            print(letter, '        ', letters[letter])
            new_file.write("\n")
            new_file.write(letter)
            new_file.write("        ")
            new_file.write(str(letters[letter]))

    new_file.close()

if __name__ == '__main__':
    main()

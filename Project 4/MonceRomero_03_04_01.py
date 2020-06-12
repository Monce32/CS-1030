# Scrabble
# Reads a list of words and calculates the points for each word

def main():

    data =  {'A': 1, 'B': 3,  'C': 3,
             'D': 2, 'E': 1,  'F': 4,
             'G': 2, 'H': 4,  'I': 1,
             'J': 8, 'K': 5,  'L': 1,
             'M': 3, 'N': 1,  'O': 1,
             'P': 3, 'Q': 10, 'R': 1,
             'S': 1, 'T': 1,  'U': 1,
             'V': 4, 'W': 4,  'X': 8,
             'Y': 4, 'Z': 10}
    my_words = []
    total = 0

    with open('1030 Project 04 01 Words.txt') as file_object:
        contents = file_object.readlines()
        for line in contents:
            next_line = line.rstrip()
            if next_line.isalpha():
                my_words.append(next_line.upper())

    new_data = points(data, my_words)
    Total = 0
    print('Word '  + '        ' + ' Points')
    for i in range(len(new_data)):
        if i % 2 == 0:
            print(new_data[i], '     ', new_data[i+1])
            total += new_data[i+1]
    print('Total:', total)

    file_object.close()

# Calculates the points from the list and our dictionary
def points(data, words):
    new_list = []
    counter = 0

    for word in words:
        if len(word) == 0 or len(word) == 10 or len(word) >= 10:
            new_list.append(word)
            new_list.append(0)
            continue
        for letter in word:
            counter += data[letter]
        new_list.append(word)
        new_list.append(counter)
        counter = 0

    return new_list

if __name__ == '__main__':
    main()

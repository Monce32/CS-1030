# Obtains multiple files within a single file and adds it to a list
# Reads through every file and outputs the contents to a single file

def main():
    data = []

    with open('1030 Project 04 03 Files.txt') as file_object:
        contents = file_object.readlines()
        for line in contents:
            if line.endswith('.txt'):
                data.append(line.rstrip())
            else:
                new_line = line.rstrip() + '.txt'
                data.append(new_line)

    file_object.close()

    file_name = 'MonceRomero 03 04 03 Output.txt'
    with open(file_name, 'a') as new_file:
        for file in data:
            with open(file) as file_object:
                contents = file_object.readlines()
                for line in contents:
                    new_line = line.rstrip()
                    new_file.write(new_line)
                    new_file.write('\n')

    file_object.close()
    new_file.close()

if __name__ == '__main__':
    main()

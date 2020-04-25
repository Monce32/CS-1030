# Program that prints Celsius and Farenheit temp from 0 to 100 in
# multiples of 10

def main():
    print("Celsius to Fahrenheit")
    print(" Conversion Table\n")

    print("Celsius    Fahrenheit")

    for cels in range(0, 101, 10):
        fahr = int((cels * 9 / 5) + 32)
        print("  " ,cels,  "       "  ,fahr)


if __name__ == '__main__':
    main()

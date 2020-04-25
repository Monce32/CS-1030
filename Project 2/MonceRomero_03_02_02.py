
from random import randint

def main():
    number = input("How many simulations would you like to run? ")
    if number == '' or number == '0' or number[0] == '-':
        exit()

    max_toss = 0
    heads = 'H H H '
    tails = 'T T T '
    my_coin = ''
    x = 0
    number = int(number)
    total_toss = []

    while x < number:
        while True:
            side = str((randint(1,2)))
            if side == '1':
                my_coin += 'H '
            elif side == '2':
                my_coin += 'T '

            max_toss += 1
            if tails in my_coin or heads in my_coin:
                print("Simulation number:", x + 1)
                print(my_coin)
                print("Flips in current simulation:", max_toss)
                total_toss.append(max_toss)
                my_coin = ''
                max_toss = 0
                break

        x += 1

    highest_coin_toss(total_toss)

def highest_coin_toss(toss):
    total = 0

    for number in toss:
        total += number
        new_total = total / len(toss)
    print("Average number of flips:", new_total)

    print("Maximum number of flips", max(toss))
    print("Minimum number of flips", min(toss))

if __name__ == '__main__':
    main()

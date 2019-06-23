import random
def main():
    lottery = []
    for item in range(7):
        number = random.randint(0, 9)
        lottery.append(number)
    for num in lottery:
        print(num, end='')
main()

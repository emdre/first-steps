def main():
    file = input('Enter a .txt file name: ')
    file = open(file, 'r')
    counter = 0
    for line in file:
        if line != '':
            print(line.strip('\n'))
            counter += 1
            if counter == 5:
                break
    file.close()


main()

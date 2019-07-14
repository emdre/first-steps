def main():
    file_name = input('Enter the name of the txt file you want to open: ')
    with open(file_name, 'r') as file:
        text = file.read().split()
        words = {}
        for word in text:
            words[word] = text.count(word)
        for key, value in words.items():
            print("{}: {}".format(key, value))


main()

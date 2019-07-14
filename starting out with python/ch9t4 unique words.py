def main():
    file_name = input('Enter the name of the txt file you want to open: ')
    with open(file_name, 'r') as file:
        words = set(file.read().split())
        for word in words:
            if word.isalpha() is False:
                words.remove(word)
        print('The unique words in this file are: ' + ', '.join(str(char) for char in words))


main()

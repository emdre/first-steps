def main():
    file_name1 = input('Enter the name of the first txt file you want to open: ')
    file_name2 = input('Enter the name of the second txt file you want to open: ')

    with open(file_name1, 'r') as file1:
        words1 = set(file1.read().split())
    with open(file_name2, 'r') as file2:
        words2 = set(file2.read().split())

    print('The unique words in the first file are: ' + ', '.join(str(char) for char in words1))
    print('The unique words in the first file are: ' + ', '.join(str(char) for char in words2))

    words_in_both_files = words1.intersection(words2)
    print('Here are the words found in both files: '
          + ', '.join(str(char) for char in words_in_both_files))

    words_in_file1 = words1.difference(words2)
    print('Here are the words that are only in the first file: '
          + ', '.join(str(char) for char in words_in_file1))

    words_in_file2 = words2.difference(words1)
    print('Here are the words that are only in the second file: '
          + ', '.join(str(char) for char in words_in_file2))

    words_in_one_file = words1.symmetric_difference(words2)
    print('Here are the words that are only in one of the files, but not in both: '
          + ', '.join(str(char) for char in words_in_one_file))


main()

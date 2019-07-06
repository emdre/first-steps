def main():
    text = input('Enter a message: ')
    vowels = 'AOEIYU'
    consonants = 'BCDFGHJKLMNPRQSTVWXZ'
    vowels_count = 0
    consonants_count = 0
    for char in text.upper():
        if char in vowels:
            vowels_count += 1
        if char in consonants:
            consonants_count +=1
    print(f'The message you entered contains {vowels_count} vowel(s) and {consonants_count} consonant(s).')
main()



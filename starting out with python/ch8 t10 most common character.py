import collections

def main():
    text = input('Enter a message: ').lower()
    most_common = (collections.Counter(text).most_common(1))
    for item in most_common:
        character = item[0]
    print(f'The most common character is {character}.')

main()
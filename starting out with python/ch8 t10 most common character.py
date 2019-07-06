import collections

text = input('Enter a message: ').lower()
most_common = (collections.Counter(text).most_common(1))
print(f'The most common character is {most_common}')

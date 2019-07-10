code = {'A': '-', 'B': '.', 'C': ',',
        'D': '!', 'E': '@', 'F': '#',
        'G': '&', 'H': '$', 'I': '(',
        'J': '^', 'K': ')', 'L': '*',
        'M': '1', 'N': '0', 'O': '2',
        'P': '9', 'Q': '3', 'R': '8',
        'S': '3', 'T': '7', 'U': '4',
        'V': '6', 'W': '5', 'X': '{',
        'Y': '}', 'Z': '[', '1': '<',
        '2': '>', '3': '?', '4': ':',
        '5': ';', '6': '|', '7': '~',
        '8': '`', '9': 'z', '0': 'x',
        ',': 'c', '.': 'w', '?': 'e',
        '/': 'h', '-': 'j', '(': 'l',
        ')': '_', 'a': '+', 'b': '=',
        'c': 'd', 'd': 'F', 'e': 'R',
        'f': 'v', 'g': 'O', 'h': 'm',
        'i': 's', 'j': 'y', 'k': 'L',
        'l': 'M', 'm': 'W', 'n': 'p',
        'o': 'A', 'p': 'K', 'r': 'Z',
        's': 'C', 'q': 'I', 't': 'T',
        'u': 'V', 'v': 'D', 'w': 'S',
        'x': 'o', 'y': 'f', 'z': 'Q',
        ' ': 'E', '\n': 'B'
        }

file_to_encrypt = open('my_name.txt', 'r+')
file_to_decrypt = open('encrypted_text.txt', 'w')
text_file = file_to_encrypt.read()
encrypted_message = ''
for ch in text_file:
    encrypted_message += code[ch]
file_to_decrypt.write(encrypted_message)
file_to_decrypt.close()
file_to_encrypt.close()

encrypted_file = open('encrypted_text.txt', 'r')
encrypted_message = encrypted_file.read()
key_value_pairs = list(code.items())
decrypted_message = ''
for char in encrypted_message:
    for i in range(len(key_value_pairs)):
        if key_value_pairs[i][1] == char:
            index = i
    decrypted_message += key_value_pairs[index][0]
encrypted_file.close()
print(decrypted_message)

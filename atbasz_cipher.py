alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z'
]

reverse_alphabet = [
    'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
    'e', 'd', 'c', 'b', 'a'
]
print("Welcome to Atbash Cipher. Type Your word or sentence.")
word = input("Pass the word:\n").lower()

for letter in word:
    final_word = ''
    if letter in alphabet:
        position = alphabet.index(letter)
        position = int(position)
        reversed_position = reverse_alphabet[position]
        final_word = reversed_position
        print(final_word, end='')
    else:
        final_word += letter
        print(final_word, end='')

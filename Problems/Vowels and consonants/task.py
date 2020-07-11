from string import ascii_lowercase


def letter_checker(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in line:
        if letter in vowels:
            print('vowel')
        elif letter in ascii_lowercase:
            print('consonant')
        else:
            return


letter_checker(input())

string = input()

for char in string:
    if char.isalpha():
        if char in 'aeiou':
            print('vowel')
        else:
            print('consonant')
    else:
        break

def letters(sentence):
    count = 0
    for char in sentence:
        if char == 'e':
            count += 1
    return count

print(letters('You never get a second chance to make a first impression'))
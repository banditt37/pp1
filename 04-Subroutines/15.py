from mymath import read_number
from mymath import generate_number
print("Guessing game\nEnter the number from 1 to 9: ", end = '')
read = read_number()
generate = generate_number()
print()
print(f'Your number: {read}\nRandom number: {generate}')
if read == generate:
    print('\nSuccess')
else:
    print('\nFail')

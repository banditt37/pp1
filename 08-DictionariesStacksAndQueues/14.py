#14.	Write a program that spells any text entered from the keyboard, using ICAO spelling alphabet (https://en.wikipedia.org/wiki/NATO_phonetic_alphabet). Create a dictionary where you put all the letters and the corresponding words. Then try to spell your name and three other words.

alphabet = {
  "A": "Alfa",
  "B": "Bravo",
  "C": "Charlie",
  "D": "Delta",
  "E": "Echo",
  "F": "Foxtrot",
  "G": "Golf",
  "H": "Hotel",
  "I": "India",
  "J": "Juliett",
  "K": "Kilo",
  "L": "Lima",
  "M": "Mike",
  "N": "November",
  "O": "Oscar",
  "P": "Papa",
  "Q": "Quebec",
  "R": "Romeo",
  "S": "Sierra",
  "T": "Tango",
  "U": "Uniform",
  "V": "Victor",
  "W": "Whiskey",
  "X": "X-ray",
  "Y": "Yankee",
  "Z": "Zulu"
}

text = str(input("Enter the text: "))
text = text.upper()

for i in text:
    for k, v in alphabet.items():
        if i == k:
            print(v)
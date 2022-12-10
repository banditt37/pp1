arr = ['SWAT', 'Cry of Fear', 'Forest Gump', 'Avatar', 'Foreigners']

file = open('filmtitles.txt', 'w')

for element in arr:
    file.write(element + "\n")

file.close()
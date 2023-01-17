#12.	Create a dictionary that describes your favourite book or film with at least five key-value pairs. Then create a program that writes the dictionary data to the favourite.json file. Use the dump() method. Note the formatting of the data in the json file. Use the 'indent' parameter in the dump() method.
import json
movie = [
    {"Title" : "The Witcher"},
    {"Creator" : "Lauren Schmidt"},
    {"Creator" : "Lauren Schmidt"},
    {"Main actor" : "Henry Cavill"},
    {"Year" : 2019},

]
with open('favourite.json', 'w') as file:
    json.dump(movie, file, indent=",")
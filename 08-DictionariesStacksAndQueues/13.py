#13.	Write a program where you create a dictionary containing student data. Try to describe a student in detail, using different data types that can be used in the dictionary. Then save the data about student in the file student.json, in a readable form.
import json
student = [
    {"Name" : "Kamil"},
    {"Group" : 2},
    {"Specialization" : "IT"}
]
with open('student.json', 'w') as file:
    json.dump(student, file)
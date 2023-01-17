import re

f = open("grades.txt")
grades = f.read()
grade = "\d.\d"
list = re.findall(grade, grades)
sum = 0.0
for i in list:
    sum+=float(i)
print(round(sum/len(list),2))
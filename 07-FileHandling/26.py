import re
f = open("tekst.txt")
fcontent = f.read()
count = "[a-zA-Z]{6}"
print(re.findall(count, fcontent))
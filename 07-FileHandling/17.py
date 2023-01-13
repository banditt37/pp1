f = open("16.txt")
ff = open("copylines.txt", "wt")
for line in f:
    ff.write(line)
f.close()
f.close()
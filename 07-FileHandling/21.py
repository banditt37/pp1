f = open("power.txt", "wt")
for line in range(1, 11):
    f.write(str(line)+','+str(line**2)+','+str(line**3)+'\n')
f.close()
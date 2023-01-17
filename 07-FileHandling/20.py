import random
f = open("random.txt", "wt")

for line in range(1, 51):
    f.write(str(random.randint(100,1000))+'\n')
f.close()
import stack

n = int(input("Enter the number: "))
count = 0

while n>0:
    if n%2==0:
        stack.push(0)
        n = round(n/2)
        count+=1
    else:
        stack.push(1)
        n = round(n/2)
        count+=1

for i in range(count):
    print(stack.pop(), end = '')
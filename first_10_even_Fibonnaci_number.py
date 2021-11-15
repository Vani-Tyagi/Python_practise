#Print first 10 even fibonacci number
a=1
b=1
count =0
while count < 10:
    a = a + b
    b = a + b
    if a % 2 == 0:
        print(a)
        count += 1
    if b % 2 == 0:
        print(b)
        count += 1

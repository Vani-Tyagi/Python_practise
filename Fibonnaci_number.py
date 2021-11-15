#Print first 10 fibonacci number
a=1
b=1
print(a)
print(b)
count =0
while count < 4:   #As already printed 2 values and while loop will print 2 values everytime.And we need to print 8 values.Hence took half i.e 4
    a = a + b
    b = a + b
    print(a)
    print(b)
    count += 1
    

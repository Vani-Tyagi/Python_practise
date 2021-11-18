#he program prompt the user and ask for the number of Fibonacci numbers required to be printed
num_to_print = 9
a=1
b=1
print(a)
print(b)
a = a+b   #To make the odd number list, printing this value outside
print(a)
count = 2
while count < (num_to_print - 2):  #Since printing first 2 values already
        b = a + b
        print(b)
        a = a + b
        print(a)
        count += 2
    

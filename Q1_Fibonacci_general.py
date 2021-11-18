#he program prompt the user and ask for the number of Fibonacci numbers required to be printed
num_to_print = int(input("How many numbers do you want to print? "))
a=1
b=1
print(a)
print(b)
count = 2
if num_to_print % 2 == 0:
    while count < (num_to_print):
        a = a + b
        b = a + b
        print(a)
        print(b)
        count += 2
else:
    a = a+b   #To make the odd number list, printing this value outside
    print(a)
    while count < (num_to_print - 2):  #Since printing first 2 values already
        b = a + b
        print(b)
        a = a + b
        print(a)
        count += 2
    

#Program to guess the lucky_number and print the output as follows:
#1. If guess_num greater by 2 ,then print 'Too High'
#2. If guess_num less by 2,then print 'Too Low'
#3. If guess_num greater or lesser by 1 then print 'Almost there'
#4.Else print 'You won'

i=1
lucky_num = int(input("What is your lucky number?"))
while i > 0:
    guess_num = int(input("Guess the number: "))
    if guess_num < lucky_num - 1:
        print('Too Low')
        i+=1
    elif guess_num > lucky_num + 1:
        print('Too High')
        i+=1
    elif (guess_num == lucky_num - 1) or (guess_num == lucky_num + 1):
        print('Almost There')
        i+=1
    else:
        print('You won',lucky_num,'is correct answer')
        break


                

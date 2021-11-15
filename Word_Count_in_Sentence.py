#Program to print number of words in a user given sentence.
sent = input("Please enter any sentence to get the count of words in it: ")
words = sent.split()
#print(type(words))---> to get type of data structure
count = 0
for word in words:
    count +=1
print("Total words in given sentence are: ",count)

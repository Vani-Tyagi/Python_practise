#Program to convert user given input to twitter hashtag[Example; Input = 'python is fun'
#output: #PythonIsFun
sent = input("Please enter the string to convert into hashtag. ")

words = sent.split()
cap_word = []
for word in words:
    cap_word.append(word.capitalize())
#print(cap_word)
hashtag = ''.join(cap_word)
print("Hashtag is: ","#"+hashtag)
    
    

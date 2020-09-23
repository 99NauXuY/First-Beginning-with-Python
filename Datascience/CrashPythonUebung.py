#What is 7 to the power of 4?
print(7**4)

#Split this string: s = "Hi there Sam!" into a list.
s = "Hi there Sam!"
print(s.split())

#Use .format() to print the following string:
planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers".format(planet,diameter))

#Given this nested list, use indexing to grab the word "hello"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])

#Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

#What is the main difference between a tuple and a list?
#Tuple kann man nicht verändern

#Create a function that grabs the email website domain from a string in the form: user@domain.com
def domainGet(email):
    lst = email.split('@')
    print(lst[1])
domainGet('user@domain.com')

'''Create a basic function that returns True if the word 'dog' is contained in the input string.
Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.'''
def findDog(sentence):
    a = sentence.split()
    if("dog" in a or "Dog" in a):
        print(True)
    else:
        print(False)
findDog('Is there a dog here?')

#Zähl Anzahl der Dogs im Satz
def countDog(sentence):
    count = 0
    for listenelement in sentence.split():
        if(listenelement == 'dog' or listenelement == 'Dog'):
            count = count + 1
    return count
print(countDog('This dog runs faster than the other dog dude!'))

'''Use lambda expressions and the filter() function to filter out words
from a list that don't start with the letter 's'.'''
seq = ['soup','dog','salad','cat','great']
print(list(filter(lambda word:word[0]=="s",seq)))

'''You are driving a little too fast, and a police officer stops you.
Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
If your speed is 60 or less, the result is "No Ticket".
If speed is between 61 and 80 inclusive, the result is "Small Ticket".
If speed is 81 or more, the result is "Big Ticket".
Unless it is your birthday (encoded as a boolean value in the parameters of the function)
-- on your birthday, your speed can be 5 higher in all cases.'''
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed-=5
    if speed>80:
        print("Big Ticket!")
    elif speed>60:
        print("Small Ticket")
    else:
        print("No Ticket")
caught_speeding(81,True)
caught_speeding(81,False)

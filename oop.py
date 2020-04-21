#!python
class Animal():
    # """docstring for Animal."""
    def __init__(self):
        print("Animal Created")
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("Eating")
##inhertiance just like extends keyword in JAVA
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def bark(self):
        print("woof")
    #method overriding in python is direct
    def eat(self):
        print("DOG Eating")

myanimal = Animal()
myanimal.whoAmI()
myanimal.eat()

#creating DOG
mydog = Dog()
mydog.__init__()
mydog.eat()

#Special Methods

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    #special methods are noted by two underscores
    #string representation
    def __str__(self):
        return "Title : {}, Author : {}, Pages = {}".format(self.title,self.author,self.pages)
    #length representation
    def __len__(self):
        return self.pages

#Lets see what will happen when we print string of it
b = Book("Python","jose",200)
print(b)
#Lets see what will happen when we print len of it
print(len(b))


#ERROR and Exceptions
#Exception Handling

try:
    f = open('sample.txt','r')
    f.write("Test write to simple Test")
except:
    print("Error found")
else:
    print("SUCCESS")
finally:
    print("I always work no matter what")

#REGULAR EXPRESSIONS : used to search patterns in strings
#USED IN DJANGO for urls

import re

patterns = ["term1","term2"]
text = "This is a string with term1,not the other !"
text2 ="term1"
split_term = '@'
#Play around with below commented code to get better understanding

# for pattern in patterns:
#     print("I'm searching for :"+pattern)

    # if re.search(pattern,text):
    #     print("Match")
    # else:
    #     print("No match!")

#returns match object
match = re.search('term1',text2)
print(match.start())

email = 'user@gmail.com'
learning_split = re.split(split_term,email)
print(learning_split)

print(re.findall('match','test phrase match in middle and in end match'))

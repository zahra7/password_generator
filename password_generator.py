import string
import random

def gen():
    upperString = string.ascii_uppercase
    lowerString = string.ascii_lowercase
    digitString = string.digits
    symbolString = string.punctuation
    
    passlen = int(input("Enter the password length : "))
    
    stringList = []
    stringList.extend(list(upperString))
    stringList.extend(list(lowerString))
    stringList.extend(list(digitString))
    stringList.extend(list(symbolString))
    
    random.shuffle(stringList)
    
    password = ("".join(stringList[0:passlen]))
    print('The password is : ' , password)

gen()
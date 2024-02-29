import math
#String data type


#literal assignment
first = "Dave"
last = "Gray"

#print(type(first))
#print(type(first)= str)
#print(ininstance(first, str))

#construction function
#pizza=str("pepperoni")
#print(type(pizza))
#print(type(pizza)=str)
#print(ininstance(pizza, str))

#concatenation
fullname= first+"    "+ last
print(fullname)

fullname+="!"
print(fullname)

#casting a number to string
decade =str(1980)
print(type(decade))
print(decade)

statement ="i like rock music from the "+ decade+"s."
print(statement)

#multiplelines
multiline='''
hey,how are you?

i was just checking in.
                                 All good

'''
print(multiline)

#Escaping special characters
sentence ='i\'m back at work!\n\n\where\'s this at \\ located?'
print(sentence)

#string methods

print(first)
print(first.lower)()
print(first.upper)()
print(first)

print(multiline.litle())
print(multiline.replace("good","ok"))
print(multiline)

print(len(multiline))
multiline+= "                                  "
multiline="                                  "+multiline
print(multiline.strip())

print(len(multiline.stripe()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

#Build a menu
title="menu".upper()
print(title.center(20,"="))
print("coffee".ljust(16,".")+"$1".rjust(4))
print("muffin".ljust(16,".")+"$2".rjust(4))
print("cheesecake".ljust(16,".")+"$4".rjust(4))

print("")

#stingstring index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#some methods return boolean data
print(first.startswitch("d"))
print(first.endswitch("z"))


#Bollean dada type
myvalue= True
x=bool(False)
print(type(x))
print(isinstance(myvalue,bool))

#numeric data types

#integer type
price=100
best_price=int(80)
print(type(price))
print(isinstance(best_price,int))

#float type
gpa=3.28
y=float(1.14)
print(type(gpa))

#complex value
comp_value=5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#Built-in functions for numbers

print(abs(gpa))
print(abs(gpa*-1))

print(round(gpa))

print(round(gpa,1))


print(math.pi)
print(math.sqrt.pi(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#casting a string to a number
zipcode="10001"
zip_value=int(zipcode)
print(type(zip_value))

#Error if you attemptto cast incorrect data
#zip_value=int("NEW YORK")
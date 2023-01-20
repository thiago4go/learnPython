#Basic String Operations
astring = "Hello World"
# Length 
print(len(astring))
# First occurrence of "W" at index
print(astring.index("W"))
# Number of o's
print(astring.count("o"))
# Slicing the string into bits
print(astring[3:7])
print(astring[3:7:2])
print(astring[::-1])
# Convert everything to UPPERCASE/lowercase
print(astring.upper())
print(astring.lower())
# Check how a string starts/ends
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
# Split the string into separate strings
print(astring.split(" ")) #inside the quotes set the spliter

# While loop
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

#Function
def sum_two_numbers(a, b):
    return a + b
x = sum_two_numbers(2,3)
print(x)

#classes
class NameClass:
    variable = "any"

    def function(self):
        print("This is a message inside the class.")

NewObjectX = NameClass()
NewObjectY = NameClass()
NewObjectZ = NameClass()

NewObjectY.variable = "thing"
NewObjectZ.variable = "you want"

print(NewObjectX.variable)
print(NewObjectY.variable)
print(NewObjectZ.variable)
NewObjectZ.function()


phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
phonebook["Jane"] = 98127890 #add to dictionary["key"] = value
del phonebook["John"] #delete key and value
phonebook.pop("Jack") #delete key and value
for name, phone in phonebook.items():
    print("Phone number of %s is %d" % (name, phone))
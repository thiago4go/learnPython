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
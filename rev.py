# the easy / built in way to reverse a string.
def reversed_string(a_string):
    return a_string[::-1]
print reversed_string('The string to reverse. CIVIC.')

# here is another way to do it.
def jakesReverseMethod(firstString):
    newString = []
    index = len(firstString)
    while index:
        index -= 1
        newString.append(firstString[index])
    return ''.join(newString)

print jakesReverseMethod('The string to reverse. CIVIC.')

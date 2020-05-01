# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Mohsen'
age = 35

print(f'My name is {name} and I\'m {age}')

s = 'Hello world'
print(s.swapcase())
print(s.lower())
print(s.capitalize())
print(s.upper())
print(s.capitalize())
# String Formatting
print(s.replace('Hello', '❤'))
# String Methods
print(s.startswith('Hello'))
print(s.endswith('d'))

# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
fruit_tuple = tuple(('Apple', 'Orange'))
print(type(fruit_tuple))
print(fruit_tuple)

fruit_str = 'apple ' + 'banana '
print(type(fruit_str))
print(fruit_str)

fruit_tuple = fruit_tuple[0], 'Banana'
print(fruit_tuple)
print(type(fruit_tuple))

fruit_str = fruit_str + 'Kiwi'
print(fruit_str)

# A Set is a collection which is unordered and unindexed. No duplicate members.

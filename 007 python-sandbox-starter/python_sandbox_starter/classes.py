# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it.
# Almost everything in Python is an object


# CREATE USER CLASS
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name}, and I\'m {self.age}.'

    def has_birthday(self):
        self.age += 1


# Create Customer class
class Customer(User):
    def __init__(self, name, email, age):
        super().__init__(name, email, age)
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def greeting(self):
        return f'My name is {self.name}, and I\'m {self.age} and my balance is {self.balance}'

    def set_balance(self, balance):
        self.balance = balance
        return balance


# Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
janet = User('Janet Williams', 'janet@gmail.com', 27)

# Edit property
brad.age = 38

janet.has_birthday()

# Call method
print(janet.greeting())

# Init customer
john = Customer('John Doe', 'john@gmail.com', 40)

john.set_balance(500)

print(john.greeting())

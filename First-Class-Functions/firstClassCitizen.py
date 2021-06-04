#you can assign a function to a variable
def func():
    print("I am function func()!")

print(func())

another_name = func
print(another_name())

#you can pass a function to another function as an argument
#this is known as function composition

def inner():
    print("I am function inner()!")


def outer(function):
    function()


print(outer(inner))


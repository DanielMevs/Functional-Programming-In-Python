# When you pass a function to another function, the passed-in 
# function sometimes is referred to as a callback because a call back
# to the inner function can modify the outer function’s behavior.
#A good example of this is Python function sorted()

#by default prints in alphabetical order
animals = ["ferret", "vole", "dog", "gecko"]
sorted(animals)

#len is the callback that alters the sorted function
#to sort by the length of the strings in the input array
print(sorted(animals, key=len))

#we can override the order to sort in reverse
print(sorted(animals, key=len, reverse=True))

def reverse_len(s):
    return -len(s)

#alternatively, we can use the above callback
print(sorted(animals, key=reverse_len))
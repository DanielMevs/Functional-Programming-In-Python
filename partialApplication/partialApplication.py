from functools import partial 

def add(x, y, z):
	return x + y + z

def add_partial(x):
	def add_others(y, z):
		return x + y + z

	return add_others

add_5 = add_partial(5)
print(add_5(6, 7))

def add_partial2(x, y):
	def add_others(z):
		return x + y + z

	return add_others

add_5_and_6 = add_partial2(5, 6)
print(add_5_and_6(7))

#curring: where the arguments of a function are applied on at a time
#until all the arguments are applied and the final result is returned.

def curry_add(x):
	def curry_add_inner(y):
		def curry_add_inner2(z):
			return x + y + z
		return curry_add_inner2
	return curry_add_inner

add_5 = curry_add(5)
add_5_and_6 = add_5(6)
add_5_6_and_7 = add_5_and_6(7)
print(add_5_6_and_7)

add_5 = partial(add, 5) 
print(add_5(6, 7))


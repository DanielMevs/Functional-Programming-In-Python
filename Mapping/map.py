x = [1, 2, 3, 4, 5, 6, 7]
def double(x):
	return x * 2

doubled = list(map(double, x))
print(doubled)
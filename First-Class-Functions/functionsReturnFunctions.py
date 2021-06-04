#a function can be defined within the scope of another
#function and can return that function as well.

def create_printer():
    def printer():
        print('Hello functional!')

    return printer

my_printer = create_printer()
my_printer()

def create_multiplier(a):
    def multiplier(x):
        return x * a

    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(5))
print(triple(6))
print(quadruple(7))

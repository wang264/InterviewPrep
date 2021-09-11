# https://www.w3schools.com/python/python_iterators.asp
# https://www.geeksforgeeks.org/difference-between-iterator-vs-generator/


# WHY we need them. save RAM/Memory. We dont need to store them in advance, only generate them when we need it.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#
# Technically, in Python, an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().

class MyNumbers:
    def __init__(self, start=1, max_size=10, step=1):
        self.max_size = max_size
        self.val = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        x = self.val
        self.val += self.step
        if x > self.max_size:
            raise StopIteration
        else:
            return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))

for i in MyNumbers(start=1, max_size=10, step=2):
    print(i)


# generator
# It is another way of creating iterators in a simple way where it uses the keyword “yield” instead of returning
# it in a defined function.

def sq_numbers(n):
    for i in range(1, n + 1):
        yield i * i


a = sq_numbers(3)

print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))

for i in sq_numbers(6):
    print(i)

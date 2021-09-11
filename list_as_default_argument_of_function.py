# In Python, is list a good choice for default argument for a function? Why
# NO
#
# https://docs.python-guide.org/writing/gotchas/

def append_to(element, to=[]):
    to.append(element)
    return to


my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)


# what you expect
# [12]
# [42]

# #what actually happen
# [12]
# [12, 42]

# Python’s default arguments are evaluated once when the function is defined, not each time the function is called
# (like it is in say, Ruby). This means that if you use a mutable default argument and mutate it, you will and have
# mutated that object for all future calls to the function as well.

# What You Should Do Instead
# Create a new object each time the function is called, by using a default arg to signal that no argument was
# provided (None is often a good choice).

def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to



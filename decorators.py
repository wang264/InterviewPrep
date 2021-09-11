# https://realpython.com/primer-on-python-decorators/


# Functions are First-Class Objects
# In Python, functions are first-class objects. This means that functions can be passed around and
# used as arguments, just like any other object (string, int, float, list, and so on).
# Consider the following three functions:

def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


greet_bob(say_hello)

greet_bob(be_awesome)


# Inner Functions
# It’s possible to define functions inside other functions. Such functions are called inner functions.
# Here’s an example of a function with two inner functions:

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


parent()


#
# Returning Functions From Functions
# Python also allows you to use functions as return values. The following example returns one of the inner
# functions from the outer parent() function:

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

first

second


# Simple Decorators
# Now that you’ve seen that functions are just like any other object in Python, you’re ready to move on and see
# the magical beast that is the Python decorator. Let’s start with an example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee_before_after = my_decorator(say_whee)

say_whee()
say_whee_before_after()

say_whee
say_whee_before_after

##########################################################################################
# Put simply: decorators wrap a function, modifying its behavior.
###########################################################################################
# Before moving on, let’s have a look at a second example. Because wrapper() is a regular Python function, the
# way a decorator modifies a function can change dynamically. So as not to disturb your neighbors, the following
# example will only run the decorated code during the day:

from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep

    return wrapper


def say_whee():
    print("Whee!")


say_whee = not_during_the_night(say_whee)

say_whee()


#
# Syntactic Sugar!
# The way you decorated say_whee() above is a little clunky. First of all, you end up typing the name say_whee
# three times. In addition, the decoration gets a bit hidden away below the definition of the function.
#
# Instead, Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie”
# syntax. The following example does the exact same thing as the first decorator example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")

say_whee()


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")


say_whee()
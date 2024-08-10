'''
def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("hello world")


def add(a, b):
    print(a + b)

# Testing the functions
hello()
add(3, 4)
'''

import logging

def log_function_call(fun):
    def decorated(*args,**kwargs):
        logging.info(f"calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = fun(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a+b




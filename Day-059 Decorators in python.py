def greet(fx):
    def mfx(*args, **kwargs):  # args - argument as tuple, kwargs -argument as dict
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx


@greet
def hello():
    print("Hello world")


@greet
def add(a, b):
    print(a + b)


# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)






# import logging
#
# logging.basicConfig(level=logging.INFO)  # configure logging to show INFO messages
#
# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated
#
# @log_function_call
# def my_function(a, b):
#     return a + b
#
# # Example run
# print(my_function(5, 10))   # Will log info and also print the result

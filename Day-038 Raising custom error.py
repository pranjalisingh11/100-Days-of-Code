# a = int(input("Enter any value between 5 and 9:"))
#
# if(a<5  or a>9):
#   raise  ValueError("Value should be between 5 and 9")



# we can made custom error
# class CustomError(Exception):
#     pass
#
# try:
#     raise CustomError("This is a custom error!")
# except CustomError as e:
#     print("Caught:", e)

a = input("Enter any value between 5 and 9: ")
try:
    if (int(a) < 5 or int(a) > 9):
        raise ValueError("Value should be between 5 and 9")

except:
    if a == str(a) and a != "quit":
        raise ValueError("Value should be between 5 and 9")

print("code ended successfuly")
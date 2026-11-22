#Exception

# try:
#     a=5
#     b=0
#     print(a/b)
# except Exception as e:
#     print("Error occured is:",e)

# print("Welcome")

# try:
#     a=int(input("Enter:"))
#     b=2
#     print(a/b)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except TypeError:
#     print("Type error occurs")
# except ValueError:
#     print("Value error")
# finally:
#     print("Code will be executed")

# print("welcome")

age=int(input("Age="))
# if age<18:
#     raise(ValueError("Age should be greater than or equal to 18"))

class Myerror(Exception):
    pass
if age<18:
        raise(Myerror("Age should be greater than or equal to 18"))


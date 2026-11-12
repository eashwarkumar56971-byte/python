# function
# def greet():
#     print("Hello world")

# greet()
# greet()

# def sum(a,b):
#     print(a+b)

# sum(4,2)
# sum(4,3)
# sum(9,8)
# sum(3,4)

#square of a number

# def square(a):
#     print("Square=",a*a)

# num=int(input("Enter the number:"))
# square(num)

#multiply 4 numbers

# def multiply(A,b,c,d):
#     print(A*b*c*d)

# multiply(2,3,1,7)


# def sum(a=0,b=0):  #default arguement
#     print(a-b)

# # sum(3,4)  #positional
# # sum(b=3,a=4)  #keyword
# sum(b=4)

#factorial of a number uusing function

# def fact(a):
#     fact=1
#     for i in range(1,a+1):
#         fact=fact*i
#     print("Factorial=",fact)

# num=int(input("Enter the number:"))
# fact(num)



# def sum (a,b):
#     return(a+b,"mohan","hi")

# sum(2,3)
# print(sum(2,3))


def sum(a,b):
    return(a+b)
def  sub(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def div(a,b):
    return(a/b)

def main():
    while True:
        print("!!!Welcome!!!")
        x=int(input("Enter the number:"))
        y=int(input("Enter the number:"))
        ch=int(input("Enter your choice.The choices are \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Exit"))
        if ch==1:
            print(sum(x,y))
        elif ch==2:
            print(sub(x,y))
        elif ch==3:
            print(multiply(x,y))
        elif ch==4:
            print(div(x,y))
        elif ch==5:
            break
        else:
            print("Invalid character")

main()



   
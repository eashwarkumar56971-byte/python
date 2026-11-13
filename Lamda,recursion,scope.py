#lamda function
# z= lambda n:n**2
# print(z(2)) 
# s=lambda x,y,z:x+y+z
# print(s(3,4,5))

#product of 3 numbers
# p=lambda x,y,z:x*y*z
# print(p(3,2,1))

#area of a triangle
# area=lambda b,h:(1/2)*b*h
# print(area(4,3))

#perimeter of a circle
# perimeter=lambda r:2*3.14*r
# print(perimeter(2))

#square root of a number
# root=lambda n:n**(1/2)
# print(root(4))

#Average of 5 numbers
# avg=lambda a,b,c,d,e:(a+b+c+d+e)
# print(avg(1,2,3,2,2)/5)

# #fullname of a person
# fullname=lambda first,middle,last:first+" "+middle+" "+last
# print(fullname("Akshay", "T", "S"))
# print(fullname("Eashwar","P","Kumar"))

#to check given person is eligible to vote

# eligibility=lambda age :"eligible"if age>=18 else "not eligible"

# print(eligibility(23))
# print(eligibility(14))

#recursion
# def count(n):
#     print(n)
#     if n==0:
#         return
#     return(count(n-1))

# count(10)

#sum of first 10 numbers

# def count(n,sum):
    
#     sum=sum+n
    
#     if n==10:
#         print("Sum=",sum)
#         return
#     return(count((n+1),sum))

# count(1,sum=0)



            #or

# def count(n):
#     if n==0:
#         return 0
#     return n+count(n-1)
# print(count(10))


#factorial using recursion

# def fact(n):
#     if n==1:
#         return 1
        
        
#     return n*fact(n-1)
# x=int(input("Enter the number"))
# print("Factorial=",fact(x))

#hw find all prime numbers between an interval



#scope of a variable

name="mohan"                               #global
def myname():
    name="mohan"                            #enclosed
    def nickname():
        name="gowri"
                              #local
        print(name)
    nickname()



(myname())





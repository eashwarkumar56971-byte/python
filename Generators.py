# def add(*args):
#     print(args)
#     sum=0
#     for i in args:
#         sum+=i
#     print("SUM=",sum)


# add(2,3,5,3,2,1,5,6,7,6,4)

# def fullname(*args,**kwargs):
#     print(args)
#     print(kwargs)


# fullname(1,2,3,4,5,3,3,2,2,4,5,5,6,firstname="mohan",mname="kumar",lname="akshay")


# def fullname(fname,mname,lname):
#     print(fname+" "+mname+" "+lname)


# fullname("mohan","J","Akshay")
# def totaltime(fun):
#     def wrapper(*args,**kwargs):
#         print(args)
#         fun(*args,**kwargs)
#     return wrapper

        






# @totaltime
# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
    
# add(2,4,5,4,5)

#generator

# def infinite():
#     i=1
#     while True:
#         yield i
#         i+=1

# b=infinite()
# print(type(b))
# for i in b:
#     if i%2==0:
#         print(i)

# import sys

# a=[]
# for i in range(0,10000000):
#     a.append(i)


# def infinte():
#     for i in range(0,10000000000):
#         yield i

# b=infinte()
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
    

        
    




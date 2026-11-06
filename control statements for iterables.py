# a="mohanraj"
# b=[2,3,5,6,6,7,0]
# c=(2,3,5,3,)

# for i in b:
#     print(i)

# for i in range(0,len(a)):
#     print(i)

# for i in range (0,len(c)):
#     print(i,c[i])

# for i in range(0,len(a)):
#     print(i,a[i])
# for i in range(len(b)):
#     print(i,b[i])

#membership operator
#print vowels and their position from the given string

# data=input("Enter the character")
# b=data.lower()
# vowel="aeiou"

# print(len(data))
# for i in range (0,len(data)):
#     if data[i]=="a"or data[i]=="e"or data[i]=="i"or data[i]=="o" or data[i]=="u":
#         print(data[i],"at index",i)
# for i in range(0,len(b)):
#     if b[i]in vowel:
#         print(b[i],"at index",i)

#create a list of 100 numbers

# list=[]

# for i in range(0,100):
#     list.append(i+1)
   
# print(list)


#create a list of even and odd numbers

# listeven=[]
# listodd=[]

# for i in range(1,101):
#     if i%2==0:
#         listeven.append(i)
#     else:
#         listodd.append(i)

# print(listeven)
# print(listodd)

# b=[1,2,3,4,5,4,3,2,1,1,1,1,2,2,2,3,3,3,4,4,5,6]
# a=[]

# print(a)
# for i in range(0,len(b)):
#         if b[i]  not in a:
#             a.append(b[i])

# print(a)

#check if a number is prime or not


# num=int(input("Enter the number:"))
# count=0
# for i in range(2,num):
#     if num%i==0:
#         count=count+1
# if num==0 or num==1:
#     print("Neither prime nor composite")
# elif count==0:
#     print("prime")
# else:
#     print("composite")
    
#to reverse a list

# list1=[]
# size=int(input("Enter the size"))
# for i in range(0,size):
#     num=int(input("Enter the number"))
#     list1.append(num)
# print(list1)
# list2=[]
# for i in range(0,len(list1)):
#     list2.append(list1[len(list1)-1-i])

# print(list2)
    


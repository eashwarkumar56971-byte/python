#for loop
# for i in range(0,100,2):
#     print(i)

# for i in range(0,11):
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(20,0,-1):
#        print(i)

#sum of first 10 numbers

# sum=0
# for i in range(1,11,1):
#     sum=sum+i

# print("Sum=",sum)

#factorial of a number
# fact=1
# num=int(input("Enter the number:"))
# for i in range(1,num+1,1):
#     fact=fact*i
# print("Factorial=",fact)

#find the sum and avg of n numbers

# count=int(input("Enter the count of numbers to find:"))
# sum=0
# for i in range(count):
#     num=int(input("Enter the number:"))
#     sum=sum+num

# Avg=sum/count
# print("Sum=",sum)
# print("Avg=",Avg)

#check if a number is amstrong or not
num=int(input("Enter the number:"))
orgnum=num
n=num
sum=0
count=0
while n!=0:
    count=count+1
    n=n//10
print(count)
while orgnum!=0:
    b=orgnum%10


    sum=sum+b**count
    orgnum=orgnum//10
print(sum)
print(num)

if num==sum:
    print("Given number is amstrong")
else:
    print("Given number is not amstrong")

    





#operator overloading
# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __add__(self, otr):
#         t1=self.m1+otr.m1
#         t2=self.m2+otr.m2
#         return t1,t2
#     def __sub__(self,otr):
#         sub1=self.m1-otr.m1
#         sub2=self.m2-otr.m2
#         return sub1,sub2
#     def __mul__(self, otr):

#         mul1=self.m1*otr.m1
#         mul2=self.m2*otr.m2
#         return mul1,mul2
#     def __truediv__(self, otr):
#         div1=self.m1/otr.m1
#         div2=self.m2/otr.m2
#         return div1,div2
#     def __gt__(self, otr):
#         t1=self.m1>otr.m1
#         t2=self.m2>otr.m2
#         return t1,t2

        


        

        


# s1=Student(16,8)
# s2=Student(4,4)
# print(s1+s2)
# print(s1-s2)
# print(s1*s2)
# print(s1/s2)
# print(s1>s2)


#method overloading

# class A:
#     def __init__(self):
#         pass
#     def hello(self,a,b):
#         return(a+b)
#     def hello(self,a,b,c):
#         return(a+b+c)
#     def hello(self):
#         print("hello")

# a=A()
# a.hello(2,3,4)                  #error
# a.hello(2,5)


#method overriding
# class A:
#     def __init__(self):
#         pass
#     def hello(self):
#         print("A says hello")

# class B(A):
#     def __init__(self):
#         pass
#     def hello(self):
#         print("B says hello")
#         super().hello()

# b=B()
# b.hello()

from abc import ABC, abstractmethod
# class Payment(ABC):
#     def __init__(self):
#         pass
#     @abstractmethod
#     def pay(self):
#         print("Paymment done")
# class Upi(Payment):
#     def pay(self):
#         print('Payment through upi')
# class Card(Payment):
#     def pay(self):
#         print("Payment through card")

# cash=Card()
# cash.pay()



# class Animal(ABC):
#     def __init__(self):
#         pass
#     @abstractmethod
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def __init__(self):
#         pass
#     def sound(self):
#         print("woff woff")

# d=Dog()
# d.sound()


# Q).Write a Python class Queue that implements a basic queue data structure with the enqueue
#  and dequeue methods. 
# The enqueue method should add an element to the rear of the queue, and the dequeue
#  method should remove and return the remaining element from the queue.
# Additionally, include a method is_empty to check if the queue is empty.
    

class Queue:
    def __init__(self):
        self.list=[]

        
        
    def enqueue(self,enque):
        self.list.append(enque)
        return self.list
    def dequeue(self):
        self.list.pop(0)
        print(self.list)
    def is_empty(self):
        if self.list==[]:
            print("True")

        else:
            print("False")
            

q=Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.dequeue()
q.is_empty()
q.dequeue()
q.is_empty()
q.enqueue(5)
q.enqueue(12)
q.enqueue(7)
q.dequeue()
q.is_empty()
        
        

        
        




        
        






                




        
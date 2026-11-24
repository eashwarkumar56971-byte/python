#inheritance
# 3 types:
#single level
#multi level
#multiple

#single level

# class Person1():   #parent class/super class
#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read")
#     def write(self):
#         print("person can write")
# class Person2(Person1):  #child class
#     def __init__(self):
#         pass
#     def run(self):
#         print("Person can run")
#     def jump(self):
#         print("Person can jump")

    


# person1=Person1()
# person1.read()
# person2=Person2()

# person2.write()
# person2.jump()

#multi level


# class Person1():   #parent class/super class
#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read")
#     def write(self):
#         print("person can write")
#     def speak(self):
#         print("Person1 can speak")

# class Person2(Person1):  #child class
#     def __init__(self):
#         pass
#     def run(self):
#         print("Person can run")
#     def jump(self):
#         print("Person can jump")
#     def speak(self):
#             print("Person2 can speak")
            
# class Person3(Person2):
#     def __init__(self):
#         pass
#     def fly(self):
#         print("Person can fly")
#     def speak(self):
#                 print("Person3 can speak")
                
    
# class Person4(Person3):
#     def __init__(self):
#         pass
#     def swim(self):
#         print("Person can swim")
#     def speak(self):
#                 print("Person4 can speak")
                
# p4=Person4()

# p3=Person3()

# p4.speak()

#multiple inheritance


# class Person1():   #parent class/super class
#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read")
#     def write(self):
#         print("person can write")
#     def speak(self):
#         print("Person1 can speak")

# class Person2():  #child class
#     def __init__(self):
#         pass
#     def run(self):
#         print("Person can run")
#     def jump(self):
#         print("Person can jump")
#     def speak(self):
#             print("Person2 can speak")
            
# class Person3():
#     def __init__(self):
#         pass
#     def fly(self):
#         print("Person can fly")
#     def speak(self):
#                 print("Person3 can speak")
                
    
# class Person4(Person1,Person2,Person3):
#     def __init__(self):
#         pass
#     def swim(self):
#         print("Person can swim")
#     # def speak(self):
#     #             print("Person4 can speak")

# p4=Person4()
# p4.speak()


class student:
    division="10B"
    def __init__(self,nam,m1,m2,m3,m4,m5):
        print("class has been created")
        self. name=nam
        self. mark1=m1
        self. mark2=m2
        self.  mark3=m3
        self.  mark4=m4
        self. mark5= m5
    def sum(self):
         
         sum=self.mark1+self.mark2+self.mark3+self.mark4+self.mark5
         print(f"{self.name} got {sum} marks")
         return sum
         
    def avg(self):
        sum=self.mark1+self.mark2+self.mark3+self.mark4+self.mark5
        avg=sum/5
        print(f"{self.name} has an avg of {avg} marks")
        return avg

    def change_name(self,nam):
        self.name=nam
        return self.name

    @classmethod

    def change_div(div):
        div.division="8B"

    @staticmethod
    def factorial():
        print("hello")



s1=student("mohan",45,33,36,46,32)

s1.change_div()
print(s1.division)

s1.avg()                    #getter

print(s1.change_name("das")) #setter
s1.factorial()

                



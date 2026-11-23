#object oriented programming

# class Car:    #class
#     def start(): #methods
#         print("Car has started")
#     def stop():
#         print("Car has stopped")

# Car1=Car
# Car1.start()
# Car1.stop()
# Car2=Car
# Car2.stop()

# class Car:
#     def __init__(self):
#         print("Car created")
#         self.name="bmw"
#         self.color="black"
#     def start(self):
#         print("Car started")
#     def stop(self):
#         print("Car stopped")

# Car1=Car()
# print(Car1.color)
# Car2=Car()
# Car2.start()
# print(Car2.name)

# class Car:
#     def __init__(self,nam,col,year):
      

    #     self.name=nam
    #     self.color=col
    #     self.year=year
    #     print(f"{self.name} is created")
    # def start(self):
    #     print(f"{self.name} has started")
    # def stop(self):
    #     print(f"{self.name} has stopped")
    # def check(self,otr):
    #     print(self.name)
#         print(otr.name)

# Car1=Car("swift","black",1990)
# # print(Car1.color)
# # print(Car1.year)
# Car2=Car("Toyota","white",1987)
# Car2.check(Car1)
# Car2.start()


class student:
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
        print(f"{self.name} got an average of {avg} marks")
    def display(self):
        sum=self.mark1+self.mark2+self.mark3+self.mark4+self.mark5
        avg=sum/5
        print(f"Name={self.name},mark1={self.mark1},mark2={self.mark2},mark3={self.mark3},mark4={self.mark4},mark5={self.mark5}")
        print(f"sum={sum},avg={avg}")

stu1=student("mohan",34,45,23,14,32)
print(stu1.name)
stu1.sum()
stu1.avg()
stu1.display()






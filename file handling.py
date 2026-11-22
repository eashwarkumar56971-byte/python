#file handling
# file1=open("hello txt","r")
# print(file1.read())
# file1.close()
# file2=open("demo txt","w")  #w overwrites
# file2.write("good morning")

# file2.close()

# file3=open("hi txt","a")        #a=append
# for i in range(1,10000001):
#     file3.write(f"\n hello{i}")

# file3.close()

# with open ("hi txt","r") as f:
#       print (f.read())    

# path="C:\\Users\\eashw\\OneDrive\\Desktop\\file txt.txt"
# with open(path,"r") as f:
#     print(f.read())

import os
# os.mkdir("welcome")
# os.rename("demo txt","die txt")
# os.remove("hello txt")
pat="C:\\Users\\eashw\\OneDrive\\Desktop\\SUSTAINABLE ENGINEERING"

if os.path.exists("hello"):
    if os.path.isfile:
        print("file")
    elif os.path.isdir:
        print("folder")
    else:
        print("not exists")
        


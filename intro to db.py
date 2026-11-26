import sqlite3

conn=sqlite3.connect("first.db")  #to connect to the db
cursor=conn.cursor()   #to interact with db

# cursor.execute('''
#                CREATE TABLE IF NOT EXISTS STUDENT(
#                 name VARCHAR(20),
#                 roll INTEGER,
#                 address TEXT
#                 )
                
#                 ''')
# cursor.execute(
#                '''
#                INSERt INTO STUDENT(name,roll,address)
#                values("mohan",20,"kochi"),("das",10,"kollam"),("akshay",22,"kottayam"),
#                ("kiran",6,"kakkanad")
               

#                 '''
#               )


cursor.execute('''
 select*from student             ''')
data=cursor.fetchall()
print(data)
for i in data:
    print(i[0],i[1],i[2])

conn.commit()
conn.close()

# conn=sqlite3.connect("second.db")
# cursor=conn.cursor()
# cursor.execute('''
#                CREATE TABLE  Employees(
#                name VARCHAR(20),
#                roll INTEGER,
#                address TEXT

#                 )''')
# conn.close()


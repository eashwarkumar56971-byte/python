import sqlite3

conn=sqlite3.connect("task.db") 
cursor=conn.cursor()

cursor.execute('''

    CREATE TABLE if not exists TASKS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20),
    des TEXT
    )
    ''')
def addtasks():
    conn=sqlite3.connect("task.db")
    cursor=conn.cursor()
    tname=input("enter taskname:")
    tdes=input("enter des")
    cursor.execute('''
              INSERT INTO Tasks (name,des)
              VALUES(?,?)

              ''',(tname,tdes))

    conn.commit()
    conn.close()
    print("Tasks added")
def viewtasks():
    conn=sqlite3.connect("task.db")
    cursor=conn.cursor()
    cursor.execute('''
            select * from TASKS 
            ''')
    data=cursor.fetchall()
    if data :
        print("Tasks found")
        for i in data:

            print(f"{i[0]}____taskname {i[1]}___taskdes {i[2]}")
    else:
        print("Tasks not found.Add tasks")

    conn.commit()
    conn.close()
def searchtasks():
 
  conn=sqlite3.connect("task.db")
  cursor=conn.cursor()
  tid=int(input("enter task id:"))
  cursor.execute('''
            SELECT * FROM tasks where id=?
  ''',(tid,))

  task=cursor.fetchone()
  if task:
      print("task found")
      print(f"{task[0]}, {task[1]},{task[2]}")
  else:
      print("no such task")

  

  

  






def main():
    print("Welcome to task management")
    while True:
        ch=int(input("Enter your choice\n1.add task,\n2.view task,\n 3.searchtasks"))
        if ch==1:
            addtasks()
        elif ch==2:
            viewtasks()
        elif ch==3:
            searchtasks()
        else:
            break
main()



     
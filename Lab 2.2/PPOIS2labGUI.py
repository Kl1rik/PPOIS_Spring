import sqlite3
import tkinter as tk
from tkinter import N, S, E, W
from tkinter import TOP, BOTTOM, LEFT, RIGHT, END, ALL
from tkinter import *
my_path = "C:\\Users\\kiril\\OneDrive\\Документы\\GitHub\\PPOIS_Spring\\Lab 2.2\\PPOIS2lab.db"
con = sqlite3.connect(my_path)
cursor = con.cursor()
my_way = tk.Tk()
val_1 = 20
val_2 = 10
f = open("C:\\Users\\kiril\\OneDrive\\Документы\\GitHub\\PPOIS_Spring\\Lab 2.2\\P.TXT","r+")


def Display_Groups(my_w,cur,val):
    my_w.title("Таблица с опт")
    my_w.geometry("1200x720") 
    r_set=cur.execute('SELECT * from Students4 WHERE GroupNumber = ?',(val,))
    i=0 # row value inside the loop 
    for student in r_set: 
        for j in range(len(student)):
            e = tk.Label(my_w, width=10, fg='blue',text=student[j],anchor='w') 
            e.grid(row=i, column=j,padx=2) 
        i=i+1
    b1 = tk.Button(my_w,  text='121701', width=10, 
               command=lambda: Display_Groups(my_way,cursor,121701))  
    b1.grid(row=35,column=1)
    
    b2 = tk.Button(my_w,  text='121702', width=10, 
               command=lambda: Display_Groups(my_way,cursor,121702))
    b2.grid(row=35,column=3)  

    b3 = tk.Button(my_w,  text='121703', width=10, 
               command=lambda: Display_Groups(my_way,cursor,121703))  
    b3.grid(row=35,column=5)     
    my_w.mainloop()


def Display_rows(my_w,cur,val1,val2):
    my_w.title("Таблица с опт")
    my_w.geometry("1200x250") 
    
    r_set=cur.execute('SELECT * from Students4 LIMIT ?,? ',(val1,val2,))

    i=0 # row value inside the loop 
    for student in r_set: 
        for j in range(len(student)):
            e = tk.Label(my_w, width=10, fg='blue',text=student[j],anchor='w') 
            e.grid(row=i, column=j,padx=2) 
        i=i+1
    b1 = tk.Button(my_w,  text='1', width=10, 
               command=lambda: Display_rows(my_way,cursor,0,10))  
    b1.grid(row=15,column=1)
    
    b2 = tk.Button(my_w,  text='2', width=10, 
               command=lambda: Display_rows(my_way,cursor,10,10))
    b2.grid(row=15,column=3)  

    b3 = tk.Button(my_w,  text='3', width=10, 
               command=lambda: Display_rows(my_way,cursor,val_1,val_2))  
    b3.grid(row=15,column=5)    

    b4 = tk.Button(my_w,  text='4', width=10, 
               command=lambda: Display_rows(my_way,cursor,30,10))  
    b4.grid(row=15,column=7)
    
    b5 = tk.Button(my_w,  text='5', width=10, 
               command=lambda: Display_rows(my_way,cursor,40,10))
    b5.grid(row=15,column=9)  
    
    my_w.mainloop()
    

def Find(my_w):
    my_w.title("Поиск студента")
    my_w.geometry("400x250") 

    l2 = tk.Label(my_w,  text='Name: ', width=10,anchor="c" )  
    l2.grid(row=4,column=1) 
    # add one text box

    options = StringVar(my_w)
    options.set("") # default value

    opt1 = OptionMenu(my_w, options, "Anton")
    opt1.grid(row=4,column=2)

    group = options.get() 
    f.write('%s' % group +'\n')
    b1 = tk.Button(my_w,  text='1', width=10, 
               command=lambda: Display_find(my_way,cursor,group))  
    b1.grid(row=11,column=1)    

    my_w.mainloop()
    
def Display_find(my_w,cur,my_group):
    my_w.title("Найденные студенты")
    my_w.geometry("1200x250") 
    r_set = cur.execute('SELECT * FROM Students4 WHERE FullName=?',(my_group,))
    i=0 # row value inside the loop 
    for student in r_set: 
        for j in range(len(student)):
            e = tk.Label(my_w, width=10, fg='blue',text=student[j],anchor='d') 
            e.grid(row=i, column=j,padx=2) 
        i=i+1
    
    my_w.mainloop()

# def Display_rows(my_w,cur,val1,val2):
#     my_w.title("Таблица с опт")
#     my_w.geometry("1000x250") 
#     r_set=cur.execute('SELECT * from Students4 LIMIT ?,?',(val1,val2,))
#     i=0 # row value inside the loop 
#     for student in r_set: 
#         for j in range(len(student)):
#             e = tk.Label(my_w, width=10, fg='blue',text=student[j],anchor='w') 
#             e.grid(row=i, column=j,padx=2) 
#         i=i+1
#     b1 = tk.Button(my_w,  text='1', width=10, 
#                command=lambda: Display_rows(my_way,cursor,10,20))  
#     b1.grid(row=11,column=1)
    
    
#     my_w.mainloop()


# Display_rows(my_way,cursor,val_1,val_2)
# Display_button(my_way)
Find(my_way)
# Display_Groups(my_way,cursor,121702)





























































# table = """CREATE TABLE Students2(
#     FullName CHAR, 
#     GroupNumber INT(5), 
#     Sem1 INT,
#     Sem2 INT,
#     Sem3 INT,
#     Sem4 INT,
#     Sem5 INT,
#     Sem6 INT,
#     Sem7 INT,
#     Sem8 INT,
#     Sem9 INT,
#     Sem10 INT
#     );"""
# cur.execute(table)
# def add_string_db(cons,curs):
#     counter =  50
#     sqlite_insert_query = """INSERT INTO Students2
#                             (FullName , GroupNumber, Sem1 ,Sem2 ,Sem3 ,Sem4 ,Sem5 ,Sem6 ,Sem7 ,Sem8 ,Sem9 ,Sem10 )
#                             VALUES 
#                             ('A',121701, 0 , 1 , 2 , 3 , 4 , 354 , 6 , 7 , 8 , 9)"""
#     count = curs.execute(sqlite_insert_query)
#     cons.commit()



# def show_table(cons,curs):
#     curs = cons.cursor()
#     curs.execute("SELECT * FROM Students2")
#     rows = curs.fetchall()
#     for row in rows:
#         print(row)


# print(show_table(con,cur))
# def find(cons,curs,id):
#     curs = cons.cursor()
#     if id == 1:
#         print("Find by group")
#         print("Enter Group number:")
#         val1 = int(input())
#         sqlite_find_by_range_db = """SELECT * FROM Students2 
#                                      WHERE GroupName = 121701
                                     
#                                      """
#     elif id == 2:
#         print("Find by FullName")
#         print("Enter FullName:")
#         val2 = str(input())
#         curs.execute("SELECT * FROM Students2 WHERE FullName=?",(val2,))
#     rows = curs.fetchall()
#     for row in rows:
#         print(row)
# #print(find(con,cur,2))
# def find_by_amount(cons,curs,id):
#     curs = cons.cursor()
#     if id == 1:
#         print("Find by group")
#         print("Enter Group number:")
#         #val1 = int(input())
#         curs.execute("SELECT * FROM Students2 Where Sem6 > 5")
#     elif id == 2:
#         print("Find by FullName")
#         print("Enter FullName:")
#         val2 = str(input())
#         curs.execute("SELECT * FROM Students2 WHERE FullName=?", (val2,))

#print(find_by_amount(con,cur,1))
#print(add_string_db(con,cur))
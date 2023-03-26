import sqlite3
import tkinter as tk
from tkinter import *
my_path = "C:\\Users\\kyrill\\Documents\\GitHub\\PPOIS_Spring\\Lab 2.2\\PPOIS2lab.db"
con = sqlite3.connect(my_path)
cursor = con.cursor()
my_way = tk.Tk()
val_1 = 20
val_2 = 10
f = open("C:\\Users\\kyrill\\Documents\\GitHub\\PPOIS_Spring\\Lab 2.2\\P.TXT","r+")
def Find(my_w,cur):
    my_w.title("Поиск студента")
    my_w.geometry("400x250") 
    def display_selected(choice):
        # choice = variable.get()
        # # choice = t1.get("1.0",END)
        # variable.set(choice)
        f.write(choice + '\n')
        choice = f.readlines()[-1]
        print(choice)
        
        return choice  
    # l1 = tk.Label(my_w,  text='Name: ', width=10,anchor="c" )  
    # l1.grid(row=15,column=1) 

    # t1 = tk.Text(my_w,  height=1, width=10,bg='white') 
    # t1.grid(row=15,column=2) 



    # l2 = tk.Label(my_w,  text='Name: ', width=10,anchor="c" )  
    # l2.grid(row=15,column=1) 
    # add one text box
    students = ['Anton','Anna', 'Slava','Ivan']
    variable = StringVar(my_w)
    
    

    # l2 = tk.Label(my_w,  text='Class: ', width=10 )  
    # l2.grid(row=4,column=1) 
    opt1 = OptionMenu(
        my_w, 
        variable, 
        "Anna",
        "Anton",
        "Slava",
        )
     
    opt1.grid(row=15,column=2)
    ch = variable.get()
    print(ch)
    # 2ch  = display_selected(choice)

    # variable.set(ch) 

    # b1 = tk.Button(my_w,  text='Поиск', width=10, 
    #            command=lambda : Display_find(my_way))  
    # b1.grid(row=16,column=1)    
    r_set = cur.execute("SELECT * FROM Students4 WHERE FullName=?",[variable.get()])
    i=0 # row value inside the loop 
    for student in r_set: 
        for j in range(len(student)):
            e = tk.Label(my_w, width=10, fg='blue',text=student[j],anchor='w') 
            e.grid(row=i, column=j,padx=2) 
        i=i+1
    my_w.mainloop()

def Display_find(my_w):
    my_w.title("Найденные студенты")
    my_w.geometry("1200x250") 

    
   
    con.commit()
    
    
    
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
Find(my_way,cursor)
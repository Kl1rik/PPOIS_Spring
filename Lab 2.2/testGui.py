import sqlite3
my_conn = sqlite3.connect('PPOIS2lab.db')
#print("Opened database successfully");
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("400x250") 

my_w.title("www.plus2net.com")
# add one Label 
l0 = tk.Label(my_w,  text='Add Student',
              font=('Helvetica', 16), width=30,anchor="c" )  
l0.grid(row=1,column=1,columnspan=4) 

l1 = tk.Label(my_w,  text='Name: ', width=10,anchor="c" )  
l1.grid(row=3,column=1) 

# add one text box

t1 = tk.Text(my_w,  height=1, width=10,bg='white') 
t1.grid(row=3,column=2) 

l2 = tk.Label(my_w,  text='Class: ', width=10 )  
l2.grid(row=4,column=1) 

# add list box for selection of class
options = StringVar(my_w)
options.set("") # default value

opt1 = OptionMenu(my_w, options, "Three", "Four", "Five")
opt1.grid(row=4,column=2)

l3 = tk.Label(my_w,  text='Mark: ', width=10 )  
l3.grid(row=5,column=1) 

# add one text box
t3 = tk.Text(my_w,  height=1, width=4,bg='white') 
t3.grid(row=5,column=2) 

radio_v = tk.StringVar()
radio_v.set('Female')

r1 = tk.Radiobutton(my_w, text='Male', variable=radio_v, value='Male')
r1.grid(row=6,column=2)

r2 = tk.Radiobutton(my_w, text='Female', variable=radio_v, value='Female')
r2.grid(row=6,column=3)

b1 = tk.Button(my_w,  text='Add Record', width=10, 
               command=lambda: add_data())  
b1.grid(row=7,column=2) 

my_str = tk.StringVar()
l5 = tk.Label(my_w,  textvariable=my_str, width=10 )  
l5.grid(row=3,column=3) 
my_str.set("Output")
def add_data():
     flag_validation=True # set the flag 
     my_name=t1.get("1.0",END)
     print(my_name) # read name
     my_class=options.get()    # read class
     my_mark=t3.get("1.0",END) # read mark
     my_gender=radio_v.get()   # read gender 
     # length of my_name , my_class and my_gender more than 2 
     if(len(my_name) < 2 or len(my_class)<2  or len(my_gender) < 2 ):
            flag_validation=False 
     try:
        val = int(my_mark) # checking mark as integer 
     except:
        flag_validation=False 
     
     if(flag_validation):
        my_str.set("Adding data...")
        try:
            #print("Connected to database successfully")
            my_data=(None,my_name,my_class,my_mark,my_gender)
            print(my_data)
      
            my_query="INSERT INTO student values(?,?,?,?,?,?,?,?)"
            my_conn.execute(my_query,my_data)
            my_conn.commit()
            x=my_conn.execute('''select last_insert_rowid()''')
            id=x.fetchone()
            l5.grid() 
            l5.config(fg='green') # foreground color 
            l5.config(bg='white') # background color 
            my_str.set("ID:" + str(id[0]))
            l5.after(3000, lambda: l5.grid_remove() )
            t1.delete('1.0',END)  # reset the text entry box
            t3.delete('1.0',END)  # reset the text entry box           

        except sqlite3.Error as my_error:
            l5.grid() 
            #return error
            l5.config(fg='red')   # foreground color
            l5.config(bg='yellow') # background color
            print(my_error)
            my_str.set(my_error)        
     else:
        l5.grid() 
        l5.config(fg='red')   # foreground color
        l5.config(bg='yellow') # background color
        my_str.set("check inputs.")
        l5.after(3000, lambda: l5.grid_remove() )
my_w.mainloop()

my_conn.close()
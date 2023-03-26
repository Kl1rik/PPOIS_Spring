import sqlite3
my_path = "C:\\Users\\kiril\\OneDrive\\Документы\\GitHub\\PPOIS_Spring\\Lab 2.2\\PPOIS2lab.db"

my_conn = sqlite3.connect(my_path)
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

l2 = tk.Label(my_w,  text='Group: ', width=10 )  
l2.grid(row=3,column=1) 

# add list box for selection of class
options1 = StringVar(my_w)
options1.set("") # default value

opt1 = OptionMenu(my_w, options1, 121701, 121702, 121703)
opt1.grid(row=3,column=2)

l2 = tk.Label(my_w,  text='Name: ', width=10 )  
l2.grid(row=4,column=1) 

# add list box for selection of class
options = StringVar(my_w)
options.set("") # default value

opt1 = OptionMenu(my_w, options, "Anton", "Anna", "Slava")
opt1.grid(row=4,column=2)

l3 = tk.Label(my_w,  text='sem1 ', width=10 )  
l3.grid(row=5,column=1) 

# add one text box
t3 = tk.Text(my_w,  height=1, width=4,bg='white') 
t3.grid(row=5,column=2) 

l4 = tk.Label(my_w,  text='sem2 ', width=10 )  
l4.grid(row=6,column=1) 

# add one text box
t4 = tk.Text(my_w,  height=1, width=4,bg='white') 
t4.grid(row=6,column=2) 

l5 = tk.Label(my_w,  text='sem3 ', width=10 )  
l5.grid(row=7,column=1) 

# add one text box
t5 = tk.Text(my_w,  height=1, width=4,bg='white') 
t5.grid(row=7,column=2) 

l6 = tk.Label(my_w,  text='sem4 ', width=10 )  
l6.grid(row=8,column=1) 

# add one text box
t6 = tk.Text(my_w,  height=1, width=4,bg='white') 
t6.grid(row=8,column=2)

l7 = tk.Label(my_w,  text='sem5 ', width=10 )  
l7.grid(row=9,column=1) 

# add one text box
t7 = tk.Text(my_w,  height=1, width=4,bg='white') 
t7.grid(row=9,column=2) 

b1 = tk.Button(my_w,  text='Add Record', width=10, 
               command=lambda: add_data())  
b1.grid(row=10,column=2) 

my_str = tk.StringVar()
l6 = tk.Label(my_w,  textvariable=my_str, width=10 )  
l6.grid(row=11,column=3) 
my_str.set("Output")
def add_data():
     flag_validation=True # set the flag 
     my_name=options.get()# read name
     my_group=options1.get()    # read class
     my_sem1=t3.get("1.0",END) # read mark
     my_sem2=t4.get("1.0",END) # read mark
     my_sem3=t5.get("1.0",END) # read mark
     my_sem4=t6.get("1.0",END)
     my_sem5=t7.get("1.0",END)

     if(len(my_name) < 2 or len(my_group)<2   ):
            flag_validation=False 
     try:
        val1 = int(my_group)
        val2 = int(my_sem1)
        val3 = int(my_sem2)
        val4 = int(my_sem3)
        val5 = int(my_sem4)
        val6 = int(my_sem5)
        val7 = 7
        val8 = 8
        val9 = 9
        val10 = 10
        val11 = 11
         # checking mark as integer 
     except:
        flag_validation=False 
     
     if(flag_validation):
        my_str.set("Adding data...")
        try:
            #print("Connected to database successfully")
            my_data=(my_name,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11)
            print(my_data)
      
            my_query="INSERT INTO Students4 (FullName, GroupNumber, Sem1 ,Sem2 ,Sem3 ,Sem4 ,Sem5 ,Sem6 ,Sem7 ,Sem8 ,Sem9 ,Sem10 ) values(?,?,?,?,?,?,?,?,?,?,?,?)"
            my_conn.execute(my_query,my_data)
            my_conn.commit()
            x=my_conn.execute('''select last_insert_rowid()''')
            id=x.fetchone()
            l6.grid() 
            l6.config(fg='green') # foreground color 
            l6.config(bg='white') # background color 
            my_str.set("ID:" + str(id[0]))
            l6.after(3000, lambda: l5.grid_remove() )
                    

        except sqlite3.Error as my_error:
            l6.grid() 
            #return error
            l6.config(fg='red')   # foreground color
            l6.config(bg='yellow') # background color
            print(my_error)
            my_str.set(my_error)        
     else:
        l6.grid() 
        l6.config(fg='red')   # foreground color
        l6.config(bg='yellow') # background color
        my_str.set("check inputs.")
        l6.after(3000, lambda: l6 .grid_remove() )
my_w.mainloop()

my_conn.close()
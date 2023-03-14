import sqlite3
con = sqlite3.connect("test2.db")
cur = con.cursor()
table = """CREATE TABLE Students2(
    FullName CHAR, 
    GroupNumber INT(5), 
    Sem1 INT,
    Sem2 INT,
    Sem3 INT,
    Sem4 INT,
    Sem5 INT,
    Sem6 INT,
    Sem7 INT,
    Sem8 INT,
    Sem9 INT,
    Sem10 INT
    );"""
# cur.execute(table)
def add_string_db(cons,curs):
    counter =  50
    sqlite_insert_query = """INSERT INTO Students2
                            (FullName , GroupNumber, Sem1 ,Sem2 ,Sem3 ,Sem4 ,Sem5 ,Sem6 ,Sem7 ,Sem8 ,Sem9 ,Sem10 )
                            VALUES 
                            ('A',121701, 0 , 1 , 2 , 3 , 4 , 354 , 6 , 7 , 8 , 9)"""
    count = curs.execute(sqlite_insert_query)
    cons.commit()



def show_table(cons,curs):
    curs = cons.cursor()
    curs.execute("SELECT * FROM Students2")
    rows = curs.fetchall()
    for row in rows:
        print(row)


print(show_table(con,cur))
def find(cons,curs,id):
    curs = cons.cursor()
    if id == 1:
        print("Find by group")
        print("Enter Group number:")
        val1 = int(input())
        sqlite_find_by_range_db = """SELECT * FROM Students2 
                                     WHERE GroupName = 121701
                                     
                                     """
    elif id == 2:
        print("Find by FullName")
        print("Enter FullName:")
        val2 = str(input())
        curs.execute("SELECT * FROM Students2 WHERE FullName=?",(val2,))
    rows = curs.fetchall()
    for row in rows:
        print(row)
#print(find(con,cur,2))
def find_by_amount(cons,curs,id):
    curs = cons.cursor()
    if id == 1:
        print("Find by group")
        print("Enter Group number:")
        #val1 = int(input())
        curs.execute("SELECT * FROM Students2 Where Sem6 > 5")
    elif id == 2:
        print("Find by FullName")
        print("Enter FullName:")
        val2 = str(input())
        curs.execute("SELECT * FROM Students2 WHERE FullName=?", (val2,))

#print(find_by_amount(con,cur,1))
#print(add_string_db(con,cur))
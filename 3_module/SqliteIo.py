import sqlite3

##################################################################
# SQLite Read
##################################################################

def read():
    con = sqlite3.connect('./3_module/test.db')        
    cur = con.cursor()

    cur.execute('select * from TEST;')
    items = cur.fetchall()
    print(items)
    con.close()

##################################################################
# SQLlite Write
##################################################################

def insert(name, point):
    try:
        con = sqlite3.connect('./3_module/test.db')
        cur = con.cursor()
        cur.execute('insert into TEST(NAME, POINT) values (?, ?);', (name, point))
        con.commit()
        read()
    
    finally:
        con.close()
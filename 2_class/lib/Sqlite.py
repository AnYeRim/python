import sqlite3

class SqliteIo:

    def __init__(self) -> None:
        pass

    ##################################################################
    # SQLite Read
    ##################################################################

    def read(self):
        con = sqlite3.connect('./2_class/test.db')        
        cur = con.cursor()

        cur.execute('select * from TEST;')
        items = cur.fetchall()
        print(items)
        con.close()

    ##################################################################
    # SQLlite Write
    ##################################################################

    def insert(self, name, point):
        try:
            con = sqlite3.connect('./2_class/test.db')
            cur = con.cursor()
            cur.execute('insert into TEST(NAME, POINT) values (?, ?);', (name, point))
            con.commit()
            SqliteIo.read(self)
        
        finally:
            con.close()
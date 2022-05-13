import sqlite3

class SqliteIo:

    def __init__(self) -> None:
        pass

    ##################################################################
    # SQLite Read
    ##################################################################

    def select(self, file_name):
        try:
            con = sqlite3.connect('./5_excel_db(xls)/test.db')        
            cur = con.cursor()

            cur.execute(f'select * from {file_name};')
            return cur.fetchall()
        
        finally:
            con.close()

    ##################################################################
    # SQLlite Write
    ##################################################################

    def insert(self, data):
    
        SqliteIo.create(self)

        coulmn_name = data[0]
        del data[0]

        try:
            con = sqlite3.connect('./5_excel_db(xls)/test.db')
            cur = con.cursor()
            cur.executemany(f'INSERT INTO VOC_20210817({coulmn_name[0]}, {coulmn_name[1]}, {coulmn_name[2]}) VALUES(?,?,?)', data)
            con.commit()
        
        finally:
            con.close()

    ##################################################################
    # SQLlite Create
    ##################################################################

    def create(self):
        try:
            con = sqlite3.connect('.//5_excel_db(xls)/test.db')
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS VOC_20210817(refID TEXT NOT NULL, POI_ID TEXT NOT NULL, tag TEXT NOT NULL)')
            con.commit()
        
        finally:
            con.close()

    def to_array(self, rows):
        data = []
        for row in rows:
            data.append(list(row))

        return data
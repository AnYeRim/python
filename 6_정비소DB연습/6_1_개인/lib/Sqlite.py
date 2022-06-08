import sqlite3

class SqliteIo:

    def __init__(self) -> None:
        pass

    ##################################################################
    # SQLite Read
    ##################################################################

    def select(self, file_name):
        try:
            con = sqlite3.connect(file_name)        
            cur = con.cursor()

            cur.execute('''
                select 
                    --No
                    ID_POI, 

                    --지점타입, 정비차종 플래그
                    (case ID_FC when 1 then '전시장' when 2 then '서비스센터' end) as ID_FC,

                    --시도명
                    ADDR_LD,

                    --대리점명
                    NM_POI, 

                    --주소: 지번주소 or 도로명주소
                    ADDR,

                    --전화번호: 식별번호, 국번, 번호 - ex) ddd)bbb-cccc~d
                    TEL
                from T_POI_BH;
            ''')

            return cur.fetchall()
        
        finally:
            con.close()

    ##################################################################
    # SQLlite Write
    ##################################################################

    def insert(self, db_name, it):
    
        SqliteIo.create(self, db_name)

        try:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            # (ID_POI, ID_FC, TEL, NM_POI, ADDR_LD, ADDR)
            # cur.executemany('insert into T_POI_BH (ID_FC, ADDR_LD, TEL, NM_POI ,ADDR) values (?,?,?,?,?);', it)
            cur.executemany('''
                insert into T_POI_BH (ID_FC, ADDR_LD, NM_POI ,TEL, ADDR)  
                select (case ? 
                        when '전시장' then 1 
                        when '서비스센터' then 2 end),
                ?,?,?,?;
            ''', it)
            con.commit()
        
        finally:
            con.close()

    ##################################################################
    # SQLlite Create
    ##################################################################

    def create(self, db_name):
        try:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            cur.execute('''
                create table if not exists T_POI_BH
                (
                    ID_POI  integer not null,   -- max 8 digit
                    TEL     text,               -- ((TD10 * 50 + ID_TA) * 15,000 + TB11) * 10,000 + TC10
                    
                    --업종 검색용 인덱스 생성
                    ID_FC   integer,            -- 정비소 구분 id?? 1:전시장 2:서비스센터

                    --서브쿼리 배제(속도 우선)
                    NM_POI  text,
                    ADDR_LD text,
                    ADDR    text,

                    primary key(ID_POI)
                );
            ''')
            con.commit()
        
        finally:
            con.close()

    def to_array(self, rows):
        data = []
        for row in rows:
            data.append(list(row))

        return data
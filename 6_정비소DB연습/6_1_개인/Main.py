import os
from lib.Sqlite import SqliteIo
from lib.Csv import CsvIo
from lib.Excel import ExcelIo
from pathlib import Path

csv_io = CsvIo()
excel_io = ExcelIo()
sqlite_io = SqliteIo()

path = os.path.dirname(os.path.realpath(__file__))

file_name = "Ford_정비소_DB_20220531"
db_name = "Ford_DB"

##################################################################
# csv 파일 - db로 저장
##################################################################

def csv_to_db():
    # csv 읽어서 데이터 반환
    file = csv_io.read(path+"\\"+file_name+".csv")
    data = list(file)
    
    # 최상단 컬럼 삭제
    del data[0] 

    # 데이터 db로 저장
    sqlite_io.insert(path+"\\"+db_name+".db", data)

##################################################################
# db 데이터 - csv로 저장
##################################################################

def db_to_excel():
    rows = sqlite_io.select(path+"\\"+db_name+".db")
    data = sqlite_io.to_array(rows)
    data.insert(0,["No","지점타입","시도명","대리점명","주소","전화번호"])
    excel_io.write(path+"\\"+file_name+".xlsx", data)

##################################################################
# 작업할 것
##################################################################

def print_echo():
    print('----------------------------------------')
    print('Python File I/O   v0.3')
    print('----------------------------------------')
    print('0. csv 읽기 - db 저장')
    print('1. db 읽기 - excel 저장')
    print('----------------------------------------')

def inut_oper():
    ion = int(input('please, insert input number ? '))
    print("choise number : {%d}" % ion)
    return ion

def get_operation(value):
    return {
        0: csv_to_db,
        1: db_to_excel
    }.get(value, None)

print_echo()
oper = inut_oper()
fnc = get_operation(oper)

if fnc != None:
     fnc()

print("finish")
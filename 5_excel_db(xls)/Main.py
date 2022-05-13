from lib.Sqlite import SqliteIo
from lib.Csv import CsvIo
from lib.Excel import ExcelIo
from pathlib import Path

csv_io = CsvIo()
excel_io = ExcelIo()
sqlite_io = SqliteIo()

##################################################################
# txt 파일 읽기
##################################################################

def read_file(file_name):
    return open(f"./5_excel_db(xls)/{file_name}", "r", encoding='utf-8')

##################################################################
# txt 파일을 delimiter로 구분하여 배열에 저장
##################################################################

def txt_file_to_array(file, delimiter):
    data = []

    while True:
        line = file.readline()
        if not line:
            break
        line = line.strip()
        data.append(line.split(delimiter))

    file.close()

    return data
    

##################################################################
# 파일 명 반환 : 경로, 확장자 없는 파일 명
##################################################################

def get_file_name(file):
    return Path(file.name).stem

##################################################################
# txt 파일 - excel로 저장
##################################################################

def text_to_excel():
    file = read_file("VOC_20210817.txt")
    data = txt_file_to_array(file, "|")
    excel_io.write(get_file_name(file), data)

##################################################################
# excel로 저장 잘 되었는지 확인 겸 출력
##################################################################

def print_excel():
    excel_io.print("VOC_20210817")

##################################################################
# excel 파일 - csv로 저장
##################################################################

def excel_to_csv():
    data = excel_io.read("VOC_20210817")
    csv_io.write("VOC_20210817", data)

##################################################################
# csv 파일 - db로 저장
##################################################################

def csv_to_db():
    file = csv_io.read("VOC_20210817")
    data = list(file)
    sqlite_io.insert(data)

##################################################################
# db 데이터 - csv로 저장
##################################################################

def db_to_csv():
    rows = sqlite_io.select("VOC_20210817")
    data = sqlite_io.to_array(rows)
    data.insert(0,["refID","POI_ID","tag"])
    csv_io.write("VOC_20210817(2)", data)

##################################################################
# 작업할 것
##################################################################

def print_echo():
    print('----------------------------------------')
    print('Python File I/O   v0.2')
    print('----------------------------------------')
    print('0. txt 읽기 - excel 저장')
    print('1. excel 출력')
    print('2. excel 읽기 - csv 저장')
    print('3. csv 읽기 - db 저장')
    print('4. db 읽기 - csv 저장')
    print('----------------------------------------')

def inut_oper():
    ion = int(input('please, insert input number ? '))
    print("choise number : {%d}" % ion)
    return ion

def get_operation(value):
    return {
        0: text_to_excel,
        1: print_excel,
        2: excel_to_csv,
        3: csv_to_db,
        4: db_to_csv
    }.get(value, None)

print_echo()
oper = inut_oper()
fnc = get_operation(oper)

if fnc != None:
    fnc()

print("finish")
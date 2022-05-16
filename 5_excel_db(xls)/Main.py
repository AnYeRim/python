from lib.Sqlite import SqliteIo
from lib.Csv import CsvIo
from lib.Excel import ExcelIo
from pathlib import Path
import struct

csv_io = CsvIo()
excel_io = ExcelIo()
sqlite_io = SqliteIo()

init_file_name = 'VOC_20210817'
# 아래 파일은 인코딩 ANSI로 변경해야 함.
# init_file_name = 'OPENING_INFO'

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
    file = read_file(f"{init_file_name}.txt")
    data = txt_file_to_array(file, "|")
    excel_io.write(get_file_name(file), data)

##################################################################
# excel로 저장 잘 되었는지 확인 겸 출력
##################################################################

def print_excel():
    excel_io.print(f"{init_file_name}")

##################################################################
# excel 파일 - csv로 저장
##################################################################

def excel_to_csv():
    data = excel_io.read(f"{init_file_name}")
    csv_io.write(f"{init_file_name}", data)

##################################################################
# csv 파일 - db로 저장
##################################################################

def csv_to_db():
    file = csv_io.read(f"{init_file_name}")
    data = list(file)
    sqlite_io.insert(data)

##################################################################
# db 데이터 - csv로 저장
##################################################################

def db_to_csv():
    rows = sqlite_io.select(f"{init_file_name}")
    data = sqlite_io.to_array(rows)
    data.insert(0,["refID","POI_ID","tag"])
    csv_io.write(f"{init_file_name}(2)", data)

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

def write_binaryfile():
    with open(f"./test.bin", 'wb') as f:
        # data = bytes([1, 2, 3, 4, 5, 6])
        test = bytes('test', 'utf-8')
        datas = struct.pack("4sidd", test, 1, 34.4, 12.1)
        wr = f.write(datas)
        f.close    

    # a = f.read()
    

def read_binaryfile():
    with open(f"./test.bin", 'rb') as f:
        datas = f.read()
        lists = struct.unpack("4sidd", datas)
        print(lists)

def get_operation(value):
    return {
        0: text_to_excel,
        1: print_excel,
        2: excel_to_csv,
        3: csv_to_db,
        4: db_to_csv
    }.get(value, None)

# print_echo()
# oper = inut_oper()
# fnc = get_operation(oper)

write_binaryfile()
read_binaryfile()

# if fnc != None:
#     fnc()

print("finish")
from lib.Sqlite import SqliteIo
from lib.Csv import CsvIo
from pathlib import Path

csv_io = CsvIo()
sqlite_io = SqliteIo()

##################################################################
# txt 파일 읽기
##################################################################

def read_file(file_name):
    return open(f"./4_excel_db/{file_name}", "r", encoding='utf-8')

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
# txt 파일 - csv로 저장
##################################################################

# file = read_file("VOC_20210817.txt")
# data = txt_file_to_array(file, "|")
# csv_io.write(get_file_name(file), data)

##################################################################
# csv 파일 - db로 저장
##################################################################

# file = csv_io.read("VOC_20210817")
# data = list(file)
# sqlite_io.insert(data)

##################################################################
# db 데이터 - csv로 저장
##################################################################

rows = sqlite_io.select("VOC_20210817")
data = sqlite_io.to_array(rows)
csv_io.write("VOC_20210817(2)", data)
import csv
import json
from lib2to3.pytree import type_repr
import os
import sqlite3

print('Python File I/O   v0.1')

#################################################################
# class  - today
#################################################################

##################################################################
# CSV File Write
##################################################################
def csv_write():    
    f = open('./1_input_output/aaaa.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f, delimiter=',')
    wr.writerow(['번호', '이름', '점수'])
    wr.writerow(['1', '안예림', '100'])
    wr.writerow(['2', '홍길동', '200'])
    wr.writerow(['3', '임꺽정', '300'])
    wr.writerow(['4', '공민구', '400'])
    wr.writerow(['5', '이지복', '500'])
    wr.writerow(['6', '공우빈', '600'])
    wr.writerow(['7', '이종민', '700'])
    wr.writerow(['8', '함수희', '800'])
    wr.writerow(['9', '조윤행', '900'])
    f.close

##################################################################
# CSV File Read
##################################################################
def csv_read():
    fr = open('./1_input_output/aaaa.csv', 'r', encoding='utf-8')
    wr = csv.reader(fr, delimiter=',')
    # ls = list(wr)
    #print(ls)
    for item in wr:
        print(item)
    fr.close

##################################################################
# JSON File Read
##################################################################
def json_read():
    json_data = {
       "head": ["번호", "이름", "점수"],
        "data" : [
            {'no': "1", 'name': "안예림A", 'point': "100"},
            {'no': "2", 'name': "안예림B", 'point': "100"},
            {'no': "3", 'name': "안예림C", 'point': "100"},
            {'no': "4", 'name': "안예림D", 'point': "100"},
            {'no': "5", 'name': "안예림E", 'point': "100"}
        ]
    }

    # 파이썬 객체인 상태
    print(json_data)

    # 파이썬 객체를 Json 문자열로 변환하여 출력
    dump_data = json.dumps(json_data, ensure_ascii=False)
    print(dump_data)

    # Json 문자열을 파이썬 객체로 변환하여 출력
    print(json.loads(dump_data))

##################################################################
# JSON File Save
##################################################################
def json_save():
    json_data = {
       "head": ["번호", "이름", "점수"],
        "data" : [
            {'no': "1", 'name': "안예림A", 'point': "100"},
            {'no': "2", 'name': "안예림B", 'point': "100"},
            {'no': "3", 'name': "안예림C", 'point': "100"},
            {'no': "4", 'name': "안예림D", 'point': "100"},
            {'no': "5", 'name': "안예림E", 'point': "100"}
        ]
    }

    with open('./1_input_output/aaaa.json', 'w', encoding="UTF-8") as writefile:
        # 파이썬 객체를 Json 파일에 저장
        json.dump(json_data, writefile, ensure_ascii=False, indent=4)

##################################################################
# JSON File Read
##################################################################
def json_read():
    
    with open('./1_input_output/aaaa.json', 'r', encoding="UTF-8") as readfile:
        try:
            # Json 파일을 파이썬 객체로 불러오기
            json_data = json.load(readfile)
            # 파이썬 객체인 상태로 출력
            print(json_data)
            # 파이썬 객체를 Json 문자열로 변환하여 출력
            print(json.dumps(json_data, ensure_ascii=False, indent=4))
        except ValueError as e:
            print(e)     

##################################################################
# SQLite Read
##################################################################
def sqlite_read():

    con = sqlite3.connect('./1_input_output/test.db')

    cur = con.cursor()
    cur.execute('select * from TEST;')
    items = cur.fetchall()
    print(items)

    con.close()


    # with open('test.db', 'r', encoding="UTF-8") as readfile:
    #     sqlite3.adapt
    #     readfile

##################################################################
# SQLite Write
##################################################################
def sqlite_write():

    con = sqlite3.connect('./1_input_output/test.db')

    cur = con.cursor()
    cur.execute('insert into TEST values (6, "홍길동C", 500);')
    con.commit()

    con.close()

##################################################################
# command line input - 숙제
##################################################################
# csv_write()
# csv_read()
# json_save()
# json_read()
sqlite_write()
sqlite_read()




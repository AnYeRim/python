from lib.Sqlite import SqliteIo
from lib.Csv import CsvIo
from lib.Json import JsonIo

csv_io = CsvIo()
json_io = JsonIo()
sqlite_io = SqliteIo()


def print_echo():
    print('----------------------------------------')
    print('Python File I/O   v0.1')
    print('----------------------------------------')
    print('0. csv_io.write()')
    print('1. csv_io.read()')
    print('2. json_io.save()')
    print('3. json_io.read()')
    print('4. sqlite_io.insert()')
    print('5. sqlite_io.read()')
    print('----------------------------------------')


def inut_oper():
    ion = int(input('please, insert input number ? '))
    print("choise number : {%d}" % ion)
    return ion

def get_operation(value):
    return {
        0: csv_io.write,
        1: csv_io.read,
        2: json_io.save,
        3: json_io.read,
        4: sqlite_io.insert,
        5: sqlite_io.read
    }.get(value, None)

print_echo()
oper = inut_oper()
fnc = get_operation(oper)

if fnc != None:
    fnc()

print("finish")
 

# switch(oper) {
#     case 0:
#         break;
#     case 1:
#         break;
#     case 2:
#         break;
#     case 3:
#         break;
#     case 4:
#         break;
#     case 5:
#         break;
#     default: 
#         break;
# }
# if oper == 0:
#     csv_io.write()
# elif oper == 1:
#     csv_io.read()
# elif oper == 2:
#     json_io.save()
# elif oper == 3:
#     json_io.read()
# elif oper == 4:
#     sqlite_io.insert("임꺽정", 600)
# elif oper == 5:
#     sqlite_io.read()
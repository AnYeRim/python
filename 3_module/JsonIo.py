import json

##################################################################
# JSON File Save
##################################################################

def save():
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

    with open('./3_module/aaaa.json', 'w', encoding="UTF-8") as writefile:
        json.dump(json_data, writefile, ensure_ascii=False, indent=4)

##################################################################
# JSON File Read
##################################################################

def read():
    with open('./3_module/aaaa.json', 'r', encoding="UTF-8") as readfile:
        try:
            json_data = json.load(readfile)
            print(json.dumps(json_data))
        except ValueError as e:
            print(e)     

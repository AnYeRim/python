
import csv

##################################################################
# CSV Input & Ouput
##################################################################

class CsvIo:

    def __init__(self) -> None:
        pass

    ##################################################################
    # CSV File Write
    ##################################################################

    def write(self):    
        f = open('./2_class/point.csv', 'w', encoding='utf-8', newline='')
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

    def read(self):
        fr = open('./2_class/point.csv', 'r', encoding='utf-8')
        wr = csv.reader(fr, delimiter=',')
        ls = list(wr)
        #print(ls])
        for item in ls:
            print(item)
        fr.close
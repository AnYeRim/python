
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
 
    def write(self, file_name, data):    
        f = open(file_name, 'w', encoding='utf-8', newline='')
        wr = csv.writer(f, delimiter=',')
        wr.writerows(data)
        f.close
        
        print('Csv로 저장 완료')

    ##################################################################
    # CSV File Read
    ##################################################################

    def read(self, file_name):
        fr = open(file_name, 'r', encoding='utf-8')
        wr = csv.reader(fr, delimiter=',')
        fr.close

        return wr


        
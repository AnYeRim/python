
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
        f = open(f"./4_excel_db(csv)/{file_name}.csv", 'w', encoding='utf-8', newline='')
        wr = csv.writer(f, delimiter=',')
        wr.writerows(data)
        f.close

    ##################################################################
    # CSV File Read
    ##################################################################

    def read(self, file_name):
        fr = open(f"./4_excel_db(csv)/{file_name}.csv", 'r', encoding='utf-8')
        wr = csv.reader(fr, delimiter=',')
        fr.close

        return wr


        
from utils.csv.CsvFileReader import CsvFileReader
from suumo.Home import Home

def test():
    reader = CsvFileReader().read('data3.csv')
    master = []
    print('-------------------------master-----------------------')
    for row in reader:
        master.append(Home(row))
        print(row['name'])


    print('-------------------------newdata-----------------------')
    reader = CsvFileReader().read('data5.csv')
    newdata = []
    for row in reader:
        newdata.append(Home(row))
        print(row['name'])

    print('-------------------------処理開始-----------------------')
    for i in newdata:
        flg = False
        for d in master:
            if i == d:
                flg = True
        if flg == False:
            master.append(i)

    for i in master:
        print(i.name)
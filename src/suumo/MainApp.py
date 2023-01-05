from suumo.SuumoApp2 import SuumoApp2
from suumo.Home2 import Home2
from utils.csv.CsvFileReader import CsvFileReader
from utils.csv.CsvFileWriter import CsvFileWriter
from logging import getLogger

import logging
formatter = "%(asctime)s:%(funcName)s:%(message)s"
logging.basicConfig(level=logging.INFO, format=formatter)

logger = getLogger(__name__)
FileName = 'newdata2.csv'
class MainApp():
    def main(self):
        logger.info('-------------------------Suumoサイトへの接続開始-----------------------')
        suumo = SuumoApp2()
        newdata = suumo.newlist()


        reader = CsvFileReader().read(FileName)
        master = []
        logger.info('-------------------------master読み込み開始-----------------------')
        for row in reader:
            master.append(Home2(row))
        logger.info('-------------------------master読み込み終了({}件)-----------------------'.format(len(master)))

        logger.info('-------------------------追加処理開始({}件)-----------------------'.format(len(newdata)))
        for i in newdata:
            flg = False
            for d in master:
                if i == d:
                    flg = True
                    break
            if flg == False:
                master.append(i)
                logger.info('{}の情報を追加しました。'.format(i.name))


        writer = CsvFileWriter()
        writer.write(FileName, master)
        logger.info('-------------------------masterを更新しました-----------------------')
        print('END')

if __name__ == '__main__':
    app = MainApp()
    app.main()
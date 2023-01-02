
from utils.web.WebReader import WebReader
from logging import getLogger
from summo.Home import Home
import logging
formatter = "%(asctime)s:%(funcName)s:%(message)s"
logging.basicConfig(level=logging.INFO, format=formatter)
logger = getLogger(__name__)


class SuumoApp():
    def get_alldata(self):
        """
        URLを解析して、そのページの情報をすべて取得して返す。
        """
        logger.debug({
            'action': 'start',
        })
        url = 'https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=030&bs=011&ta=13&jspIdFlg=patternShikugun&sc=13123&kb=1&kt=10000&mb=50&mt=9999999&ekTjCd=&ekTjNm=&tj=0&kr=A&cct=003&cn=9999999&srch_navi=1'
        result = WebReader().get_html(url)
        logger.info({
            'action': 'success',
            'result': {
                'type': type(result),
                'size': len(result)
            }
        })
        return result


    def get_homes(self, alldata):
        """
        物件情報毎に分割して返す。
        """
        logger.debug({
            'action': 'start',
        })
        result = alldata.find_all('div', {'class': 'property_unit-content'})
        logger.info({
            'action': 'success',
            'result': {
                'type': type(result),
                'size': len(result)
            }
        })
        return result
    
    def get_home_dict(self, home):
        """
        1件の住宅情報を受け取り、dictにして返す
        """
        logger.debug({
            'action': 'start',
        })
        result = {}
        for i in home.find_all('div', {'class': 'dottable-line'}):
            dt = i.find_all('dt')
            dd = i.find_all('dd')
            
            for j in range(len(dt)):
                vdt = dt[j].text
                vdd = dd[j].text
                result[vdt] = vdd
                
        logger.debug({
            'action': 'success',
            'result': {
                'type': type(result),
                'size': len(result)
            }
        })
        return result


suumo = SuumoApp()
alldata = suumo.get_alldata()
homes = suumo.get_homes(alldata)
csvs = []
for home in homes:
    dict = suumo.get_home_dict(home)
    csvs.append(Home(dict))

for csv in csvs:
    print(csv)
# for csv in csvs:
#     print(csv['物件名'])
#     print(csv['販売価格'])
#     print(csv['所在地'])
#     print(csv['沿線・駅'])
#     print(csv['専有面積'])
#     print(csv['間取り'])
#     print(csv['バルコニー'])
#     print(csv['築年月'])

print('END')

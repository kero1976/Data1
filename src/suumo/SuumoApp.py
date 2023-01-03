
from utils.web.WebReader import WebReader
from logging import getLogger
from suumo.Home import Home

logger = getLogger(__name__)


class SuumoApp():
    def get_alldata(self):
        """
        URLを解析して、そのページの情報をすべて取得して返す。
        """
        logger.debug({
            'action': 'start',
        })
        url = 'https://suumo.jp/jj/bukken/ichiran/JJ012FC001/?ar=030&bs=011&cct=003&cn=9999999&ekTjCd=&ekTjNm=&et=15&kb=1&kr=A&kt=3500&mb=50&mt=9999999&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13121&sc=13122&sc=13123&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13120&sc=13116&sc=13117&sc=13119&ta=13&tj=0&po=0&pj=1&pc=100'

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


    def newlist(self):
        logger.debug({
            'action': 'start',
        })
        alldata = self.get_alldata()
        homes = self.get_homes(alldata)
        result = []
        for home in homes:
            dict = self.get_home_dict(home)
            result.append(Home(dict))
        logger.info({
            'action': 'success',
            'result': {
                'size': len(result)
            }
        })
        return result

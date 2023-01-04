
from utils.web.WebReader import WebReader
from logging import getLogger
from suumo.Home import Home
from utils.DebugUtil import DebugUtil
import re

logger = getLogger(__name__)

import logging
formatter = "%(asctime)s:%(funcName)s:%(message)s"
logging.basicConfig(level=logging.INFO, format=formatter)

class SuumoApp2():
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
    
    def get_home_url(self, home):
        """
        1件の住宅情報を受け取り、urlを取得する
        """
        logger.info({
            'action': 'start',
        })
        result = None
        for i in home.find_all('h2', {'class': 'property_unit-title'}):
            url = i.find_all('a')
            for j in url:
                link = j.get('href')
                result = WebReader().get_html('https://suumo.jp{}'.format(link))
        logger.info({
            'action': 'success',

        })
        return result

    def detail_get(self, data):
        logger.info({
            'action': 'start',
        })
        result = None
        result =  data.find_all('div', {'class': 'section_h2-body js-acc_contents'})
        self.detail_get_name(result[3])
        self.detail_get_table(result[3])

    def detail_get_name(self, data):
        outer = data.find_all('div',{'class': 'secTitleOuterR'})
        inner = outer[0].find_all('h3',{'class': 'secTitleInnerR'})
        result = inner[0].string
        logger.debug({
            'action': 'success',
            'result': result
        })
        return result

    def detail_get_table(self, data):
        table = data.find_all('tbody',{'class': 'vat tal'})
        self.detail_get_table_1(table[0])

    def detail_get_table_1(self, data):
        tr = data.find_all('tr')
        self.detail_get_table_1_row3(tr[2])
        self.detail_get_table_1_row4(tr[3])
        self.detail_get_table_1_row5(tr[4])


    def detail_get_table_1_row3(self, data):
        """
        価格
        管理費
        """
        th = data.find_all('th')
        td = data.find_all('td')
        price_name = self._get_th_value(th[0])
        kanrihi_name = self._get_th_value(th[1])
        price_val = self._get_td_value(td[0])
        kanrihi_val = self._get_td_value(td[1])
        result = {}
        result[price_name] = price_val
        result[kanrihi_name] = kanrihi_val
        logger.info({
            'action': 'success',
            'result': result
        })
        return result

    def detail_get_table_1_row4(self, data):
        """
        修繕積立金
        """
        th = data.find_all('th')
        td = data.find_all('td')
        name = self._get_th_value(th[0])
        val = self._get_td_value(td[0])
        result = {}
        result[name] = val
        logger.info({
            'action': 'success',
            'result': result
        })
        return result

    def detail_get_table_1_row5(self, data):
        """
        諸費用
        間取り
        """
        th = data.find_all('th')
        td = data.find_all('td')
        price_name = self._get_th_value(th[0])
        kanrihi_name = self._get_th_value(th[1])
        price_val = self._get_td_value(td[0])
        kanrihi_val = self._get_td_value(td[1])
        result = {}
        result[price_name] = price_val
        result[kanrihi_name] = kanrihi_val
        logger.info({
            'action': 'success',
            'result': result
        })
        return result

    def _get_th_value(self, th):
        print(th)
        val = th.find_all('div')
        result = val[0].string
        logger.debug({
            'action': 'success',
            'result': result
        })
        return result

    def _get_td_value(self, td):
        val = td.children
        for i in val:
            result = re.sub('\s', '', i)
            break
        logger.info({
            'action': 'success',
            'result': result
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
            alldata = self.get_home_url(home)
            self.detail_get(alldata)
            break
            
        logger.info({
            'action': 'success',
            'result': {
                'size': len(result)
            }
        })
        return result

suumo2 = SuumoApp2()
suumo2.newlist()
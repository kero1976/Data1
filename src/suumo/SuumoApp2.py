
from utils.web.WebReader import WebReader
from logging import getLogger
from suumo.Home2 import Home2
from utils.DebugUtil import DebugUtil
import re

logger = getLogger(__name__)

import logging
formatter = "%(asctime)s:%(levelname)s:%(funcName)s:%(message)s"
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
        logger.debug({
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
            'result': link

        })
        return result

    def detail_get(self, data):
        logger.debug({
            'action': 'start',
        })
        result = {}
        tables =  data.find_all('div', {'class': 'section_h2-body js-acc_contents'})

        for i in tables:
            dict = self.detail_get_table(i)
            result.update(dict)

        return Home2(result)

    def detail_get_table(self, data):
        tables = data.find_all('tbody',{'class': 'vat tal'})
        result = {}
        for i in tables:
            temp = self._detail_get_table(i)
            result.update(temp)

        return result

    def _detail_get_table(self, data):
        tr = data.find_all('tr')
        list = {}
        for i in tr:
            th = i.find_all('th')
            td = i.find_all('td')
            if len(th) == len(td):
                logger.debug('正常,サイズ:{}'.format(len(th)))
                for i in range(len(th)):
                    key = self._get_th_value(th[i])
                    val = self._get_td_value(td[i])
                    list[key] = val
            else:
                logger.debug('異常、サイズが一致しません')
        return list

    def _get_th_value(self, th):
        logger.debug({
            'action': 'start',
        })
        try:
            val = th.find_all('div')
            result = val[0].string
        except:
            result = th.string
        logger.debug({
            'action': 'success',
            'result': result
        })
        return result

    def _get_td_value(self, td):
        logger.debug({
            'action': 'start',
            'param': td})
        try:
            val = td.children
            for i in val:
                result = re.sub('\s', '', i)
                break
        except Exception as e:
            result = ''
        logger.debug({
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
        no = 0
        for home in homes:
            no += 1
            try:
                alldata = self.get_home_url(home)
                result.append(self.detail_get(alldata))
                logger.info({
                    'action': 'success',
                    'no': no
                })
            except Exception as e:
                logger.error({
                    'action': 'fail',
                    'no': no,
                    'e': e
                })
        logger.info({
            'action': 'success',
            'result': {
                'size': len(result)
            }
        })
        return result

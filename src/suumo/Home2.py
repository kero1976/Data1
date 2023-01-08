from dataclasses import dataclass
from utils.date.DateUtil import DateUtil
import hashlib
from logging import getLogger
from utils.money.Money import Money

logger = getLogger(__name__)

@dataclass
class Home2():
    name: str
    price: str
    location: str
    station: str
    area: str
    plan: str
    balcony: str
    build: str
    regist: str
    hashdata: str
    kanrihi: str
    shuuzen: str
    kaisu: str
    soukosu: str
    goukei: int

    def __init__(self, dict):
        try:
            self.name = dict['物件名']
            try:
                self.price = dict['販売価格'].replace('\n', '')
            except:
                self.price = dict['価格']
            self.location = dict['所在地']
            try:
                self.station = dict['沿線・駅']
            except:
                self.station = dict['交通']
            self.area = dict['専有面積']
            self.plan = dict['間取り']
            try:
                self.balcony = dict['バルコニー']
            except:
                self.balcony = dict['その他面積']
            try:
                self.build = dict['築年月']
            except:
                self.build = dict['完成時期(築年月)']
            self.regist = DateUtil.get_now_min()
            self.hashdata = hashlib.sha256((self.name + self.price + self.area).encode('utf-8')).hexdigest()
            # 追加項目
            self.kanrihi = dict['管理費']
            self.shuuzen = dict['修繕積立金']
            self.kaisu = dict['所在階']
            self.soukosu = dict['総戸数']
            self.goukei = Money.toInt(self.kanrihi) + Money.toInt(self.shuuzen)
        except Exception as e:
            try:
                self.name = dict['name']
                self.price = dict['price']
                self.location = dict['location']
                self.station = dict['station']
                self.area = dict['area']
                self.plan = dict['plan']
                self.balcony = dict['balcony']
                self.build = dict['build']
                self.regist = dict['regist']
                self.hashdata = dict['hashdata']
                self.kanrihi = dict['kanrihi']
                self.shuuzen = dict['shuuzen']
                self.kaisu = dict['kaisu']
                self.soukosu = dict['soukosu']
                if dict.get('goukei'):
                    self.goukei = dict['goukei']
                else:
                    self.goukei = Money.toInt(self.kanrihi) + Money.toInt(self.shuuzen)
            except Exception as e:
                logger.error('Homeデータ作成でエラー', e)
    def __eq__(self, __o: object) -> bool:
        return self.hashdata == __o.hashdata
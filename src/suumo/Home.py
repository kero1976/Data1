from dataclasses import dataclass
from utils.date.DateUtil import DateUtil
import hashlib

@dataclass
class Home():
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

    def __init__(self, dict):
        try:
            self.name = dict['物件名']
            self.price = dict['販売価格'].replace('\n', '')
            self.location = dict['所在地']
            self.station = dict['沿線・駅']
            self.area = dict['専有面積']
            self.plan = dict['間取り']
            self.balcony = dict['バルコニー']
            self.build = dict['築年月']
            self.regist = DateUtil.get_now_min()
            self.hashdata = hashlib.sha256((self.name + self.price + self.area).encode('utf-8')).hexdigest()
        except:
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

    def __eq__(self, __o: object) -> bool:
        return self.hashdata == __o.hashdata
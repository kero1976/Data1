import dataclasses
import datetime


@dataclasses
class Home():
    name: str
    price: str
    location: str
    station: str
    area: str
    plan: str
    balcony: str
    build: str
    regist: str = str(datetime.datetime.now())

    def __init__(self, dict):
        name = dict['物件名']
        price = dict['販売価格']
        location = dict['所在地']
        station = dict['沿線・駅']
        area = dict['専有面積']
        plan = dict['間取り']
        balcony = dict['バルコニー']
        build = dict['築年月']

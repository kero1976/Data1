
from utils.web.WebReader import WebReader

url = 'https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=030&bs=011&ta=13&jspIdFlg=patternShikugun&sc=13123&kb=1&kt=10000&mb=50&mt=9999999&ekTjCd=&ekTjNm=&tj=0&kr=A&cct=003&cn=9999999&srch_navi=1'
data = WebReader().get_html(url)

bukken = data.find_all('div', {'class': 'ui-media'})
print('len:' + str(len(bukken)))

print(bukken[0])
print('len:' + str(len(bukken)))

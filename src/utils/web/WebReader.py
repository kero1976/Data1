from requests_html import HTMLSession
from bs4 import BeautifulSoup
from logging import getLogger
from retry import retry

logger = getLogger(__name__)


class WebReader():
    """
    WEBスクレイピングクラス。
    """
    @retry(tries=5, delay=1, backoff=2)
    def get_html(self, url):
        logger.debug({
            'action': 'start',
            'params': {
                'url': url
            }
        })
        session = HTMLSession()
        r = session.get(url)
        r.html.render()
        soup = BeautifulSoup(r.text, 'lxml')
        logger.debug({
            'action': 'success'
        })
        return soup

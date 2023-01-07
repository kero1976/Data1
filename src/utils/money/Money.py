from logging import getLogger

logger = getLogger(__name__)

import logging
# formatter = "%(asctime)s:%(funcName)s:%(message)s"
# logging.basicConfig(level=logging.DEBUG, format=formatter)

class Money():
    @classmethod
    def toInt(cls, data: str) -> int:
        logger.debug({
            'action': 'start',
            'param': data
        })
  
        if data.find('無') == 0:
            logger.debug({
                'action': '"success',
                'result': 0
            })
            return 0
        # 円の後ろを切り捨てる
        price = data[0:data.find('円')]
        logger.debug({
            'action': '"run',
            'price': price
        })
        # 万が含まれているか？
        index = price.find('万')
        logger.debug({
            'action': '"run',
            'index': index
        })
        if index == 1:
            prefix = price[0:1]
            end = price[2:]
            result = '{}{:0>4}'.format(prefix, end)
        else:
            result = int(price)
        logger.debug({
            'action': '"success',
            'result': result
        })
        return int(result)

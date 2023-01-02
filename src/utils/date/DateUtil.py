from logging import getLogger
import datetime

logger = getLogger(__name__)


class DateUtil():
    @classmethod
    def get_now_min(cls):
        """
        現在時刻を分の精度で取得する。
        YYYY/MM/DD HH24:MI
        """
        logger.debug({
            'action': 'start',
        })
        d = datetime.datetime.now()
        # %Y=西暦4桁、%m=0埋めした月、%d=0埋めした日、%H=0埋めした24時間表記の時間、%M=0埋めした分
        result= d.strftime('%Y/%m/%d %H:%M')
        logger.debug({
            'action': 'success',
            'result': result
        })
        return result

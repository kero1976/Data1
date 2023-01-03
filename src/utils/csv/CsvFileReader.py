
import os
from logging import getLogger
from retry import retry
import csv
from utils.DebugUtil import DebugUtil

logger = getLogger(__name__)


class CsvFileReader():
    """
    csvファイルの書き込みクラス。
    """
    @retry(exceptions=PermissionError, tries=5, delay=1, backoff=2)
    def read(self, filepath):
        """
        CSV(SJIS)を読み込み、Dictにして返す。
        """
        logger.debug({'action': 'start', 'params': {
            'filepath': filepath,
        }})
        result = []
        with open(self._abspath(filepath), 'r', encoding='cp932') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                result.append(row)

        logger.debug({'action': 'success'
        })
        return result

    def _abspath(self, path):
        """
        絶対パスにして返す。
        """
        logger.debug({'action': 'start', 'params': {
            'path': path
        }})
        result = os.path.abspath(path)
        logger.debug({
            'action': 'success',
            'result': result
        })
        return result

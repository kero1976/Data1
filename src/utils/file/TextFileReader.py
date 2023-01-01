
import os
from logging import getLogger
from retry import retry

logger = getLogger(__name__)


class TextFileReader():
    """
    テキストファイルの読み込みクラス。
    """
    @retry(exceptions=PermissionError, tries=5, delay=1, backoff=2)
    def read(self, filepath):
        """
        テキストファイルを読み込む。
        """
        logger.debug({'action': 'start', 'params': {
            'filepath': filepath
        }})
        try:
            with open(self._abspath(filepath), 'r', encoding='cp932') as f:
                result = f.read()
                logger.debug({'action': 'success'})
                return result
        except UnicodeDecodeError as e:
            logger.debug({
                'action': 'run',
                'message': e
            })
            with open(self._abspath(filepath), 'r', encoding='utf-8') as f:
                result = f.read()
                logger.debug({'action': 'success'})
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


import os
from logging import getLogger
from retry import retry

logger = getLogger(__name__)


class TextFileWriter():
    """
    テキストファイルの書き込みクラス。
    """
    @retry(exceptions=PermissionError, tries=5, delay=1, backoff=2)
    def write(self, filepath, data):
        """
        テキストファイルをUTF-8で書き込む。
        """
        logger.debug({'action': 'start', 'params': {
            'filepath': filepath
        }})
        
        with open(self._abspath(filepath), 'w', encoding='utf-8') as f:
            f.writelines(data)
        logger.debug({'action': 'success'
        })

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

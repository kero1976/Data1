
import os
from logging import getLogger

logger = getLogger(__name__)


class FileReader():
    def read(self, filepath):
        """
        テキストファイルを読み込む。
        """
        logger.debug({'action': 'run', 'params': {
            'filepath': filepath
        }})
        with open(self._abspath(filepath), 'r') as f:
            result = f.read()
            logger.debug({'action': 'success'})
            return result

    def _abspath(self, path):
        """
        絶対パスにして返す。
        """
        logger.debug({'action': 'run', 'params': {
            'path': path
        }})
        result = os.path.abspath(path)
        logger.debug({
            'action': 'success',
            'result': result
        })
        return result

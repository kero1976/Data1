
import os
from logging import getLogger
from retry import retry
import csv

logger = getLogger(__name__)


class CsvFileWriter():
    """
    csvファイルの書き込みクラス。
    """
    @retry(exceptions=PermissionError, tries=5, delay=1, backoff=2)
    def write(self, filepath, data):
        """
        DataclassのリストをCSV(SJIS)で書き込む。
        Dataclass専用
        """
        logger.debug({'action': 'start', 'params': {
            'filepath': filepath,
            'type': type(data)
        }})
        try:
            fieldnames = data[0].__dict__.keys()
        except Exception as e:
            logger.error({
                'action': 'fail',
                'message': 'ヘッダ情報の作成に失敗しました'
            })
            raise e

        with open(self._abspath(filepath), 'w', encoding='cp932', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for d in data:
                writer.writerow(d.__dict__)
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

class DebugUtil():
    """
    デバッグ時に使用するユーティリティ
    """
    @classmethod
    def print(cls, val):
        """
        値の型とサイズを標準出力に出力する。
        """
        print('TYPE:{}'.format(type(val)))
        try:
            print('SIZE:{}'.format(len(val)))
        except:
             print('SIZE:None')
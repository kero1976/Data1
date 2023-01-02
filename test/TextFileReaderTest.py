from utils.file.TextFileReader import TextFileReader
import logging
formatter = "%(asctime)s:%(funcName)s:%(message)s"
logging.basicConfig(level=logging.DEBUG, format=formatter)
console = logging.StreamHandler()
logging.getLogger('utils').addHandler(console)


def test():
    data = TextFileReader().read('./test/data/sample1.txt')
    assert data == 'aaaa\nbbb'
    assert type(data) == str

def test_sjis():
    data = TextFileReader().read('./test/data/SJIS.txt')
    assert data == 'あああ'
    assert type(data) == str

def test_utf8():
    data = TextFileReader().read('./test/data/UTF8.txt')
    assert data == 'あああ'

def test_read_line():
    data = TextFileReader().read_line('./test/data/sample1.txt')
    assert len(data) == 2
    assert data[0] == 'aaaa'
    assert type(data) == list
from utils.file.TextFileReader import FileReader
import logging
formatter = "%(asctime)s:%(funcName)s:%(message)s"
logging.basicConfig(level=logging.DEBUG, format=formatter)

data = FileReader().read('./test/data/sample1.txt')
print('start' + data)

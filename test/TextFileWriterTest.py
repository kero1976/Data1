from utils.file.TextFileWriter import TextFileWriter
from summo.Simple import Simple
import csv
import dataclasses
from utils.DebugUtil import DebugUtil
def test():
    data = []
    data.append(Simple('ABC1', 'xyz1'))
    data.append(Simple('ABC2', 'xyz2'))
    data.append(Simple('ABC3', 'xyz3'))
    print(data)
    d = Simple('ABC', 'xyz')
    v = d.__dict__.keys()
    DebugUtil.print(v)
    fields = dataclasses.fields(d)
    

    with open('abc.txt', 'w', newline='') as csv_file:
        fieldnames = v
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        # for i in data:
            # writer.writerow(i.__dict__)
    # wr = TextFileWriter()
    # # wr.write('abc.txt', data)
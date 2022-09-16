from Types.cols import Cols
from Types.row import Row
from Types.csv import csv
from Types.num import Num

class Data:

    def __init__(self, src):
        if type(src) is str:
            self.rows = csv(src)
            self.cols = Cols(self.rows[0].cooked)
        else:
            self.rows = src
            self.cols = Cols(src[0])


    def add(self, row):
        self.rows.append(row)

    def stats(self, decimal, columns, function='mid'):
        output = {}
        for col in columns:
            nums = Num(0, 'jimothy', 512)
            for row in self.rows[1:]:
                nums.add(row.cells[col])
            if function == 'mid':
                output[columns[col]] = nums.mid()
            if function == 'div':
                output[columns[col]] = nums.div()
        return output



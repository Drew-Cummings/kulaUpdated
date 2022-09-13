from cols import Cols
from row import Row
from csv import csv
from num import Num

class Data:

    def __init__(self, src):
        if type(src) is str:
            self.rows = csv(src)
            self.cols = Cols(self.data[0])
        else:
            self.rows = src
            self.cols = Cols(src[0])


    def add(self, row):
        self.rows.append(row)

    def stats(self, decimal, columns, function):
        output = []
        for col in columns:
            col_nums = []
            for row in self.rows:
                col_nums.append(row[col])
            output.append(round(Num(col_nums).function()), decimal)
        return output



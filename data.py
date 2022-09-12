#from Cols import Cols
#from Row import Row
from main import csv

class Data:

    def __init__(self, csv):
        self.cols = []
        self.rows = csv



    def add(self, row):
        self.rows.append(row)




class Row:
    
    def __init__(self, record):
        self.cells = record  #one record
        self.cooked = record.copy()  #use if discretize the data
        self.isEvaled = False  #true if y-values evaluated

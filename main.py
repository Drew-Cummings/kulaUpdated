from eg.eg import *
from Types.csv import csv

if __name__ == '__main__':
    sample = csv('Files/auto93.csv')
    config_the = get_the(csv_help)
    config_the = cli(config_the)
    print(config_the)

    eg = Eg(config_the)
    eg.ALL()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

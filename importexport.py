from operator import itemgetter
import csv
from os.path import exists
exist = 0
def Import(filename):
    if exists(f"Textfiles/{filename}.txt") == True:
        Imported = list(csv.reader(open(f"Textfiles/{filename}.txt",'r',encoding="utf8")))
        exist = 1
        return Imported
    else:
        print(f"{filename}.txt doesn't exist")

def Export(filename, listname):
    csv.writer(open(f"Textfiles/{filename}.txt", 'w', newline='')).writerows(listname)

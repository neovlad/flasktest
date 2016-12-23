import csv,re

def get_next(code):
    reader = csv.reader(open('WIKI2.csv','rb'))
    mylist = list(reader)


    print mylist
    return mylist[0][mylist[0].index(code)+1]

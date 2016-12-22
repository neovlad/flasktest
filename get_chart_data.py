import quandl
def getdata(name,startcolumn=1,endcolumn=0):
    reqdata=quandl.get(name)

    if (endcolumn!=0):
        reqdata= reqdata[reqdata.columns[startcolumn:endcolumn]]

    return reqdata

import urllib
import pandas as pd
import zipfile


def getIndexData(date):
    link = 'http://images1.cafef.vn/data/'+date.strftime('%Y%m%d') + \
    '/CafeF.Index.Upto'+date.strftime('%d%m%Y') +'.zip'
    #fileName = 'D:\\python\\vnstock\\history.zip'
    fileName = '/tmp/history_index.zip'
    #req = urllib2.urlopen(link)
    response = urllib.urlopen(link)

    file = open(fileName, 'wb')
    file.write(response.read())
    file.close()
    frame = getDataFromFile( fileName )
    return(frame)


def getStockData(date):
    '''
    Retrieve data from cafef.vn. Input is a date, returns the dataframe.

    Data is saved at /tmp/history.zip by default.

    '''
    link = 'http://images1.cafef.vn/data/'+date.strftime('%Y%m%d') + \
    '/CafeF.SolieuGD.Upto'+date.strftime('%d%m%Y') +'.zip'
    #fileName = 'D:\\python\\vnstock\\history.zip'
    fileName = '/tmp/history.zip'
    #req = urllib2.urlopen(link)
    response = urllib.urlopen(link)

    file = open(fileName, 'wb')
    file.write(response.read())
    file.close()
    frame = getDataFromFile( fileName )
    return(frame)


def getDataFromFile(fileName):
    list_ = []
    with zipfile.ZipFile(fileName) as myzip:
        archives = [one.filename for one in myzip.filelist]
        for archive in archives:
            exchange = archive.split('.')[1]
            with myzip.open(
                    archive) as myfile:  # 'CafeF.'+exchange+'.Upto'+date.strftime('%d.%m.%Y')+'.csv') as myfile:
                data = pd.read_csv(myfile, header=0, names=['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'],
                                   parse_dates=['Date'])
                data['Exchange'] = exchange
                list_.append(data)

    frame = pd.concat(list_)
    return (frame)

#data = getData(datetime.datetime(2017,3,31,0,0))
#print(data)

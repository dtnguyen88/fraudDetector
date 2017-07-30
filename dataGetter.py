import urllib.request
import pandas as pd
import zipfile

def getData(date):
    link = 'http://images1.cafef.vn/data/'+date.strftime('%Y%m%d') + \
    '/CafeF.SolieuGD.Upto'+date.strftime('%d%m%Y') +'.zip'
    #fileName = 'D:\\python\\vnstock\\history.zip'
    fileName = '/tmp/history.zip'
    #req = urllib2.urlopen(link)
    response = urllib.request.urlopen(link)

    file = open(fileName, 'wb')
    file.write(response.read())
    file.close()
    exchanges = ['HSX','HNX']
    list_ =[]
    with zipfile.ZipFile(fileName) as myzip:
        for exchange in exchanges:
            with myzip.open('CafeF.'+exchange+'.Upto'+date.strftime('%d.%m.%Y')+'.csv') as myfile:
                data = pd.read_csv(myfile, header = 0,names = ['Ticker','Date','Open','High','Low','Close','Volume'])
                data['Exchange'] = exchange
                list_.append(data)
    frame = pd.concat(list_)
    frame['Date'] = pd.to_datetime(frame.Date, format='%Y%m%d')
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

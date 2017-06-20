import urllib.request
import pandas as pd
import datetime
import zipfile

def getData(date):
    link = 'http://images1.cafef.vn/data/'+date.strftime('%Y%m%d') + \
    '/CafeF.SolieuGD.Upto'+date.strftime('%d%m%Y') +'.zip'
    fileName = 'D:\\python\\vnstock\\history.zip'
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

#data = getData(datetime.datetime(2017,3,31,0,0))
#print(data)
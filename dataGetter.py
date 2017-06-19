def getData(date):
    link = 'http://images1.cafef.vn/data/'+date.strftime('%Y%m%d') + \
    '/CafeF.SolieuGD.Upto'+date.strftime('%d%m%Y') +'.zip'
    #'http://images1.cafef.vn/data/20170303/CafeF.SolieuGD.03032017.zip'
    #http://images1.cafef.vn/data/20170303/CafeF.SolieuGD.Upto03032017.zip
    fileName = 'D:\\python\\vnstock\\history.zip'
    req = urllib2.urlopen(link)
    file = open(fileName, 'wb')
    file.write(req.read())
    file.close()
    exchanges = ['HSX','HNX']
    list_ =[]
    with zipfile.ZipFile(fileName) as myzip:
        for exchange in exchanges:
            with myzip.open('CafeF.'+exchange+'.Upto'+date.strftime('%d.%m.%Y')+'.csv') as myfile:
                data = pd.read_csv(myfile, header = 0,names = ['Ticker','Date','Open','High','Low','Close','Volume'])
                list_.append(data)
    frame = pd.concat(list_)
    frame['Date'] = pd.to_datetime(frame.Date, format='%Y%m%d')
    return(frame)
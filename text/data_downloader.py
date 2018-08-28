import requests
import datetime

#历史TICK数据下载器
symbol_list = ['eth.usdt','btc.usdt','bch.usdt','etc.usdt','eos.usdt','ltc.usdt','xrp.usdt','ont.usdt','okb.usdt']
#下载路径
file_path = 'C:/data/'
start_date = '2018-01-01'
end_date = '2018-05-31'
date_list = []
begin_date = datetime.datetime.strptime(str(start_date),'%Y-%m-%d')
end_date = datetime.datetime.strptime(str(end_date),'%Y-%m-%d')
while begin_date <= end_date:
    date_str = begin_date.strftime("%Y-%m-%d")
    date_list.append(date_str)
    begin_date += datetime.timedelta(days=1)

for symbol in symbol_list:
    for date in date_list:
        try:
            url = 'http://alihz-net-0.qbtrade.org/hist-ticks?date=' + date + '&contract=okex/'+symbol + '&format=json'
            print(url)
            r = requests.get(url)
            filename = file_path + symbol  + date + '.gz'
            with open(filename,'wb') as f:
                f.write(r.content)
                f.close()
        except Exception as e:
            print(e)
            print(date)

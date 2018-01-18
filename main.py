import urllib.request
import ast
import time

def scrapename():
    x = urllib.request.urlopen("https://api.iextrading.com/1.0/ref-data/symbols?filter=symbol")
    x = x.read().decode('utf-8')



    x = x.split('[{')
    x = x[1].split('}]')
    x = x[0]
    x = x.split('},{')
    t = []

    for i in x:
        z = '{'+i+'}'
        t+=[z]

    s = ''
    y = []
    for i in range(len(t)):
        for b in t[i]:
            s += b
        z = ast.literal_eval(s)
        s = ''
        y.append(z.copy())

    return y
def getcurrent1():
    import pandas as pd
    import pandas.io.data as web  # Package and modules for importing data; this code may change depending on pandas version
    import datetime

    # We will look at stock prices over the past year, starting at January 1, 2016
    start = datetime.datetime(2016, 1, 1)
    end = datetime.date.today()

    # Let's get Apple stock data; Apple's ticker symbol is AAPL
    # First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
    apple = web.DataReader("AAPL", "yahoo", start, end)

    type(apple)
def getcurrent():
    print('running')
    y = scrapename()
    d = {}
    z = time.clock()
    for i in y:
        try:
            x = urllib.request.urlopen("https://api.iextrading.com/1.0/stock/{}/quote?filter=open".format(i['symbol']))

            x = x.read().decode('utf-8')


            d[i['symbol']] = ast.literal_eval(x)
        except:
            print('error')
        print(len(d))
    print(time.clock()-z)
for i in scrapename():
    print(i['symbol'])

import urllib.request
import ast

def scrape():
    x = urllib.request.urlopen("https://api.iextrading.com/1.0/ref-data/symbols")
    x = x.read().decode('utf-8')

    s = ""
    for i in x:
        if i == 't':
            s += 'T'
        elif i == 'f':
            s += 'F'
        else:
            s += i

    x = s.split('[{')
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




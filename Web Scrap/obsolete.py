# import yfinance as yf

# tickerdata = yf.Ticker('google') #the tickersymbol for Tesla
# print (tickerdata.info['sector'])

#--------------------------------------------------------------------------------------------------------------------------------------------

# from urllib.request import urlopen
# from lxml.html import parse

# '''
# Returns a tuple (Sector, Indistry)
# Usage: GFinSectorIndustry('IBM')
# '''
# def GFinSectorIndustry(name):
#   tree = parse(urlopen('http://www.google.com/finance?&q='+name))
#   print(tree.xpath)
# #   return tree.xpath("//a[@id='sector']")[0].text, tree.xpath("//a[@id='sector']")[0].getnext().text


# if __name__ == '__main__':
#     res = GFinSectorIndustry('microsoft')


#--------------------------------------------------------------------------------------------------------------------------------------------
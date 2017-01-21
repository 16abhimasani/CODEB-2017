from client2 import run

ash = run("yungSavage", "2121", "MY_CASH")
print(type(ash))


ticList = ["ANR","COKE","FORD","GM","INTL","MMM","QQ","RACE","VOD","YUM"]
bidDict = {}
askDict = {}

for elem in ticList:
    orders = run("yungSavage", "2121", "ORDERS {}".format(elem))
    # print(orders)
    ordersParse = orders.split()
    # print(ordersParse)
    tempParse = ordersParse[:]
    while "BID" in tempParse:
            bidIndex = tempParse.index("BID")
            bidPriceIndex = bidIndex + 2
            bidVolIndex = bidIndex + 3
            bidPrice = tempParse[bidPriceIndex]
            bidVol = tempParse[bidVolIndex]
            bidPriceTup = ("BID", elem, bidPrice, bidVol)
            bidVolumeVal = int(bidPriceTup[3])
            if bidVolumeVal > 1000:
                bidPriceTup = bidPriceTup + ("FAKE",)
            print(bidPriceTup)
            tempParse = tempParse[bidPriceIndex:]
    while "ASK" in tempParse:
            askIndex = tempParse.index("ASK")
            askPriceIndex = askIndex + 2
            askVolIndex = askIndex + 3
            askPrice = tempParse[askPriceIndex]
            askVol = tempParse[askVolIndex]
            askPriceTup = ("ASK", elem, askPrice, askVol)
            askVolumeVal = int(askPriceTup[3])
            if askVolumeVal > 1000:
                askPriceTup = askPriceTup + ("FAKE",)
            print(askPriceTup)
            tempParse = tempParse[askPriceIndex:]

    countBid = orders.count("BID")
    bidDict[elem] = countBid
    countAsk = orders.count("ASK")
    askDict[elem] = countAsk

print("BID", bidDict)
print("ASK", askDict)

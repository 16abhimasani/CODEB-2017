from client2 import run

# ash = run("yungSavage", "2121", "MY_CASH")
# print(type(ash))


ticStr = run("yungSavage", "2121", "SECURITIES")
ticRawList = ticStr.split()
ticRawList.remove("SECURITIES_OUT")
# print(ticRawList)

ticParse = []
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for elem in ticRawList:
    for letter in alphabet:
        if elem[0] == letter:
            ticParse.append(elem)

divDict = {}
i = 0
while (i+4) < (len(ticRawList) - 1):
    tempList = ticRawList[i:(i+4)]
    try:
        divDict[ticRawList[i]] = float(tempList[2])
    except:
        divDict[ticRawList[i]] = tempList[2]
    i += 4
# print(divDict)



# print(tic2List)


# ticList = ["AMZN","DIS","FB","GOOGL","IBM","IVW","KING","KO","NFLX","TSLA"]
#
bidDict = {}
askDict = {}
bidData = {"BID" : {}}
askData = {"ASK" : {}}

for tick in ticParse:
    orders = run("yungSavage", "2121", "ORDERS {}".format(tick))
    # print(orders)
    ordersParse = orders.split()
    # print(ordersParse)
    tempParse = ordersParse[:]
    negBidCount = 0
    negAskCount = 0

    bidData["BID"][tick] = {"Amount" : 0, "Price" : [], "Size" : []}
    askData["ASK"][tick] = {"Amount" : 0, "Price" : [], "Size" : []}

    while "BID" in tempParse:
            bidIndex = tempParse.index("BID")
            bidPriceIndex = bidIndex + 2
            bidVolIndex = bidIndex + 3
            bidPrice = tempParse[bidPriceIndex]
            bidVol = tempParse[bidVolIndex]
            bidPriceTup = ("BID", tick, bidPrice, bidVol)
            bidVolumeVal = int(bidPriceTup[3])
            if bidVolumeVal > 1000:
                bidPriceTup = bidPriceTup + ("FAKE",)
                negBidCount += 1
            else:
                bidPriceTup = bidPriceTup + ("REAL",)
            print(bidPriceTup)
            tempParse = tempParse[bidPriceIndex:]
            priceAppend = bidData["BID"][tick]["Price"]
            priceAppend.append(bidPrice)
            sizeAppend = bidData["BID"][tick]["Size"]
            sizeAppend.append(bidVol)

    while "ASK" in tempParse:
            askIndex = tempParse.index("ASK")
            askPriceIndex = askIndex + 2
            askVolIndex = askIndex + 3
            askPrice = tempParse[askPriceIndex]
            askVol = tempParse[askVolIndex]
            askPriceTup = ("ASK", tick, askPrice, askVol)
            askVolumeVal = int(askPriceTup[3])
            if askVolumeVal > 1000:
                askPriceTup = askPriceTup + ("FAKE",)
                negAskCount += 1
            else:
                askPriceTup = askPriceTup + ("REAL",)
            print(askPriceTup)
            tempParse = tempParse[askPriceIndex:]
            priceAppend = askData["ASK"][tick]["Price"]
            priceAppend.append(askPrice)
            sizeAppend = askData["ASK"][tick]["Size"]
            sizeAppend.append(askVol)

    countBid = orders.count("BID")
    bidDict[tick] = countBid - negBidCount
    bidData["BID"][tick]["Amount"] = countBid - negBidCount
    countAsk = orders.count("ASK")
    askDict[tick] = countAsk - negAskCount
    askData["ASK"][tick]["Amount"] = countAsk - negAskCount

print("------------------------------------------------------------------------------------------------")
print("BID AMOUNT", bidDict)
print("ASK AMOUNT", askDict)
print("DIV", divDict)
print("------------------------------------------------------------------------------------------------")
print(bidData)
print("------------------------------------------------------------------------------------------------")
print(askData)

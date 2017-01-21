from client2 import run

ash = run("yungSavage", "2121", "MY_CASH")
print(type(ash))


ticList = ["ANR","COKE","FORD","GM","INTL","MMM","QQ","RACE","VOD","YUM"]
bidDict = {}
askDict = {}

for elem in ticList:
    orders = run("yungSavage", "2121", "ORDERS {}".format(elem))
    print(orders)
    countBid = orders.count("BID")
    bidDict[elem] = countBid
    countAsk = orders.count("ASK")
    askDict[elem] = countAsk

print("BID", bidDict)
print("ASK", askDict)

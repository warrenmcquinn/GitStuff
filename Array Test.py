import Cryptsy

counter = 0
active = True

#Logs in
Exchange = Cryptsy.Cryptsy("Key","Secret")
#Gets the market
market = Exchange.getMarkets()
#Desired Coin
coin = raw_input("Enter desired Coin: ")

coin_list = []


while(active):
   addcoin = market['return'][counter]['primary_currency_name']
   coin_list.append(addcoin)
   counter = counter+1
   if counter==250:
        active=0
        print coin_list

for item in coin_list:
      if item == coin:
         print item

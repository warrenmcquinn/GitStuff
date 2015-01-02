import Cryptsy

counter = 0
active = True

#Logs in
Exchange = Cryptsy.Cryptsy("KEY","Secret")
#Gets the market
market = Exchange.getMarkets()
#Desired Coin
coin = input("Enter desired Coin: ")

coin_list = []


while(active):
   addcoin = market['return'][num]['primary_currency_name']
   coin_list.append(addcoin)
   num = num+1
   if num==250:
        active=0
        print coin_list

for item in temp_list:
      if item == coin
         print item

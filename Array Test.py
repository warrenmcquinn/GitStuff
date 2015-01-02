import Cryptsy

#Logs in
Exchange = Cryptsy.Cryptsy("1b17cb00a0e21c1b2dd063856edc4f3164b93107","51d77a60ab88afa1f67cb4ee1744c47120fd40960e99a43c8eac17bcc63da68bf6c64f8561fff71d")
#Gets the market
market = Exchange.getMarkets()
#Desired Coin
coin = raw_input("Enter desired Coin: ")

coin = unicode(coin)

for currency in market['return']:
	if currency['primary_currency_name'] == coin:
		print currency
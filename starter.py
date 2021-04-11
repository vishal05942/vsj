import alpaca_trade_api as tradeapi
import time

key = "<YOUR KEY HERE>"
sec = "<YOUR SECRET HERE>"

url = "https://paper-api.alpaca.markets"

api = tradeapi.REST(key, sec, url, api_version='v2')

#Init our account var
account = api.get_account()

print(account.status)
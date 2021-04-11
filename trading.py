
import alpaca_trade_api as tradeapi
import time
import pandas as pd

#current_time = pd.Timestamp().isoformat()
#print(current_time)

key = "<YOUR KEY HERE>"
sec = "<YOUR SECRET HERE>"


url = "https://paper-api.alpaca.markets"


api = tradeapi.REST(key, sec, url, api_version='v2')


account = api.get_account()

def get_num_shares(stock):
    all_pos = api.list_positions()
    i = 0
    for i in range(len(all_pos)):
        if stock == all_pos[i].symbol:
            return all_pos[i].qty
    
    return 0
print(api.list_orders(status="filled"))
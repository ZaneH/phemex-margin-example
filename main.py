# -*- coding: utf-8 -*-

import time
from src.client import Client
from dotenv import load_dotenv
import os
from pprint import pprint

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

if __name__ == "__main__":
    # Be sure this matches your testnet.phemex.com account
    # and that you have USDT & BTC in your Margin account
    # https://testnet.phemex.com/trade/BTCUSDT to transfer funds
    # it's on the far right and looks like a circle with 2 arrows
    api_key = os.getenv("PHEMEX_API_ID")
    api_secret = os.getenv("PHEMEX_API_SECRET")
    client = Client(api_key, api_secret, True)

    # Test query
    pprint(client.query_account_n_positions("BTC"))

    # Open long and close it
    try:
        pprint(client.place_order({
            "symbol": "BTCUSD",
            "clOrdID": "Test1" + str(time.time()),
            "side": "Buy",
            "orderQty": 1,
            "ordType": "Limit",
            # $43,632.00
            "priceEp": 436320000,
            "timeInForce": "GoodTillCancel",
            "posSide": "Long"
        }))

        pprint(client.place_order({
            "actionBy": "UserClosePosition",
            # TODO: must be equal to the clOrdId from above
            "clOrdID": "25e95598-6f17-605a-3cb0-e59c983475b7",
            "closeOnTrigger": True,
            "ordType": "Limit",
            "orderQty": 1,
            # $43,640.10
            "priceEp": 436401000,
            "side": "Sell",
            "symbol": "BTCUSD",
            "timeInForce": "GoodTillCancel",
        }))
    except Exception as e:
        pprint(e)

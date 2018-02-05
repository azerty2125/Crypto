import sys, os
import time
import argparse

import csv
import pandas as pd
import numpy as np

import crypto

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--params", type=str, help="file.xml", required=True)
	parser.add_argument("--loop", type=int, help="Loop time in sec (0 one shot)", default=0)
	parser.add_argument("--save", type=bool, help="Write file True/False", default=False)
	#parser.add_argument("--symbol", type=str, help="Market Symbol (Ex: XVGBTC)", default='ALL')
	option = parser.parse_args()

	clients = crypto.utils.get_clients(option.params)
	out_dir = crypto.utils.get_out_dir(option.params)

	dict_clients = {}
	for client in clients :
		dict_clients[crypto.utils.get_client_name(client)] = client

	result = crypto.market.get_all_market_prices(clients)
	# sort by maximum difference
	result.sort_values(by='delta', inplace=True, ascending=False)
	print(result.head(10))

	# Get possible transactions with more than 3% gain
	for index, row in result[(result['delta'] > 3)].iterrows():
		from_exchange = row['From']
		to_exchange = row['To']
		coin = row['pair'].split('-')[0]
		address = crypto.assets.get_deposit_address(dict_clients[to_exchange],coin)
		if address :
			print('Transfer {0} from {1} to {2} \taddress {3}'.format(coin,from_exchange,to_exchange,address))
		else :
			print('Cannot transfer {0} from {1} to {2}'.format(coin,from_exchange,to_exchange))




	# if option.loop > 0 :
	# 	while True :
	# 		market_prices = crypto.market.get_market_prices(client)
	# 		if option.save :
	# 			crypto.market.update_market_file(out_dir,market_prices)
	# 		print('Loop [ETHUSDT] {0}'.format(market_prices['ETHUSDT']))
	# 		time.sleep(option.loop)
	# else :
	# 	market_prices = crypto.market.get_market_prices(client)
	# 	print('[ETHUSDT] {0}'.format(market_prices['ETHUSDT']))



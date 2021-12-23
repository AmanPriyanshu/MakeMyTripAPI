import requests
import pandas as pd
from proxy_gen import ProxyGen
from datetime import datetime, timedelta
import random

class GenerateDatedFlightDetails:
	def __init__(self):
		self.proxies = self.get_proxies()
		self.proxy = False
		self.start_city = 'IXE'
		self.end_city = 'DOH'
		self.start_date = self.convertStr2Date('01/01/2022')
		self.end_date = self.convertStr2Date('31/01/2022')
		self.nos_days = (self.end_date - self.start_date).days

	def get_proxies(self):
		proxies = ProxyGen().proxies
		return {key:proxies[key] for key in proxies.keys() & ['IP Address', 'Port', 'Https']}

	def convertStr2Date(self, date):
		datetime_object = datetime.strptime(date, '%d/%m/%Y')
		return datetime_object

	def url_generator(self, date='10/01/2022', cabin_class='E', forwardFlowRequired=True):
		url = "https://www.makemytrip.com/flight/search?tripType=O&itinerary="+self.start_city+"-"+self.end_city+"-"+date+"&paxType=A-1_C-0_I-0&cabinClass="+cabin_class+"&forwardFlowRequired="+'true' if forwardFlowRequired else 'false'
		return url

	def extract_flight_details(self, url):
		response = requests.get(url)

	def iterate_dates(self):
		for i in range(self.nos_days):
			date = self.start_date+timedelta(i)
			date = date.strftime("%d/%m/%Y")
			url = self.url_generator(date)
			proxy_index = random.randint(0, len(self.proxies['Port']))
			print(url)
			header = {
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
			}
			if self.proxy:
				response = requests.get(url, headers=header, proxies={"http": "http://"+self.proxies['IP Address'][proxy_index]+':'+self.proxies['Port'][proxy_index], "https": "https://"+self.proxies['IP Address'][proxy_index]+':'+self.proxies['Port'][proxy_index]}, verify=False)
			else:
				response = str(requests.get(url, headers=header).content)
			with open('f.txt', 'w') as f:
				f.write(response)
			exit()

if __name__ == '__main__':
	gdfd = GenerateDatedFlightDetails()
	gdfd.iterate_dates()
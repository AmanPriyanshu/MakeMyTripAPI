import requests
import pandas as pd

class ProxyGen:
	def __init__(self):
		self.proxies = self.loadUpProxies()

	def loadUpProxies(self):
		global proxies
		url='https://sslproxies.org/'
		header = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
		}
		response=requests.get(url,headers=header)
		response = str(response.content)
		response = response[response.index('IP Address')+len('IP Address'):]
		response = response[response.index('<tbody>')+len('<tbody>'):]
		response = response[:response.index('</tbody>')]
		response = [i.replace('<tr>', '') for i in response.split('</tr>')]
		response = [i.split('</td>') for i in response]
		response = [[j[j.index('>')+1:] for j in i[:-1]] for i in response][:-1]
		columns = ['IP Address', 'Port', 'Code', 'Country', 'Anonymity', 'Google', 'Https', 'Last Checked']
		r = {}
		for col_idx, col_name in enumerate(columns):
			r.update({col_name: [i[col_idx] for i in response]})
		return r

	def saveProxies(self, filename='proxy.csv'):
		df = pd.DataFrame(self.proxies)
		df.to_csv(filename, index=False)


if __name__ == '__main__':
	p = ProxyGen()
	p.saveProxies()
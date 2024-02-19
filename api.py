import pickle

import requests

API_KEY = "BU2WE0DBU98SX76L"

symbols = []
company_details = []
with open("symbols.txt") as f:
  for i in range(25):
    symbol = f.readline().strip()
    symbols.append(symbol)
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-keye
for i in range(20):
  url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbols[i]}&apikey={API_KEY}'
  r = requests.get(url)
  data = r.json()
  company_details.append(data)

with open('company_infos.dat','wb') as fout:
  company_details = pickle.dumps(company_details)
  fout.write(company_details)

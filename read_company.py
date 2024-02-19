symbols = []
with open("company_names.csv") as f:
  data = f.readlines()
  for company in data:
    symbols.append(company.split(',')[0])
  print(symbols)

with open("symbols.txt",'w') as fin:
  fin.write('\n'.join(symbols))
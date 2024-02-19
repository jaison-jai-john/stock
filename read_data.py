import pickle

with open('company_infos.dat','rb') as f:
  data = pickle.load(f)
  for i in data:
    if len(i.keys()) != 1:
      for j in i.keys():
        print(f'{j} : {i[j]}')
import random
names=['ivan', 'dragan', 'niki']
random.shuffle(names)
c=0
for name in names:
  print(f'{1+c}. {name}')
  c+=1
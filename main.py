import random
names=[]
# name=input()
while True:
    name = input()
    if name == 'Go':
        break
    names.append(name)


# names=input().split(', ')

random.shuffle(names)
c=0
for name in names:
  print(f'{1+c}. {name}')
  c+=1
import re

with open('input.txt') as f:
  lines=[line.strip() for line in f.readlines()]

y=[]
count=0
for i,line in enumerate(lines):
  x=line.split('|')
  numbers=[ int(m.group()) for m in re.finditer('\d+', x[0])]
  card_id, numbers1=numbers[0], numbers[1:]
  numbers2=[ int(m.group()) for m in re.finditer('\d+', x[1])]
  same_numbers=len(set(numbers1) & set(numbers2))

  count+= 0 if same_numbers==0 else 2**(same_numbers-1) #for part 1

  # 1st number - how many copies does card yield, 2nd number - how many cards are there
  y.append([same_numbers, 1])
  prev=y[0:-1]
  counts=0
  for j,el in enumerate(prev):
    if prev[j][0]>0:
      prev[j][0]-=1
      counts+=prev[j][1]

  y[0:-1]=prev
  y[i][1]+=counts

print('Solution for part 1: ', count)
print('Solution for part 2: ', sum([i[1] for i in y]))

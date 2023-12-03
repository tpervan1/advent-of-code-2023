import re

with open('input.txt') as f:
  lines=[line.strip() for line in f.readlines()]

numbers_in_lines, symbols_in_lines, symbols_in_lines_star = [],[], []
for line in lines:
  positions_numbers=[(m.start(), m.end(), m.group()) for m in re.finditer('\d+', line)]
  positions_symbols=[ m.start() for m in re.finditer('[^\d.]', line)]
  positions_symbols1=[ m.start() for m in re.finditer('[*]', line)]
  numbers_in_lines.append(positions_numbers)
  symbols_in_lines.append(positions_symbols)
  symbols_in_lines_star.append(positions_symbols1)

count=0
for i,line in enumerate(numbers_in_lines):
  if i==0:
    search_space=symbols_in_lines[i : i+2]
  elif i==len(numbers_in_lines):
    search_space=symbols_in_lines[i-1 : i+1]
  else:
    search_space=symbols_in_lines[i-1 : i+2]

  search_space_pos=[j for i in search_space for j in i]
  for number in line:
    for i in range(number[0]-1, number[1]+1):
      if i in search_space_pos:
        count+=int(number[2])
        break

print('Solution for part 1: ', count)

gear_sum=0
for i,line in enumerate(symbols_in_lines_star):
  if line:
    if i==0:
      search_space=numbers_in_lines[i : i+2]
    elif i==len(symbols_in_lines_star):
      search_space=numbers_in_lines[i-1 : i+1]
    else:
      search_space=numbers_in_lines[i-1 : i+2]

    search_space_pos=[j for i in search_space for j in i]
    #display(search_space_pos)

    for gear in line:
      count=0
      gear_ratio=[]
      for number in search_space_pos:
        if gear in range(number[0]-1, number[1]+1):
          count+=1
          gear_ratio.append(int(number[2]))
        if count>2:
          count=0
          gear_ratio=[]
          break
      if len(gear_ratio)==2:
        gear_sum+=gear_ratio[0]*gear_ratio[1]

print('Solution for part 2:',gear_sum)

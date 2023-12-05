import re

def search_maps(maps,location_number):
  for map in maps:
    for ranges in map:
      if location_number>=ranges[1] and location_number<ranges[1]+ranges[2]:
        location_number+=ranges[0]-ranges[1]
        break

  return location_number


maps=[[] for i in range(8)]
i=-1
with open('input.txt') as f:
  for line in f.readlines():
    line=line.strip()
    if line:
      if line[0] in ['s', 'f', 'w', 'l', 't', 'h']:
        i+=1
    numbers=[int(m.group()) for m in re.finditer('\d+', line)]
    if numbers:
      maps[i].append(numbers)

locations=[]
for i in range(len(maps[0][0])):
  x=maps[0][0][i]
  locations.append(search_maps(maps[1:],x))

print('Solution for part 1:', min(locations))
#-----------------------------------------------

locations=[]
for i in range(0,len(maps[0][0]), 2):
  lower_bound = maps[0][0][i]
  upper_bound = maps[0][0][i]+maps[0][0][i+1]
  for j in range(lower_bound, upper_bound, round((upper_bound-lower_bound)/10000)):
    x=j
    locations.append((search_maps(maps[1:],x),j))

min_value=min(locations)
print('\nFirst guess - final value and starting value:', min_value)

#get staring range
for i in range(0,len(maps[0][0]), 2):
  if min_value[1]>maps[0][0][i] and min_value[1]<maps[0][0][i]+maps[0][0][i+1]:
    starting_range=maps[0][0][i],maps[0][0][i]+maps[0][0][i+1]
    break

print('\nStarting range for search:', starting_range)

locations=[]
lower_bound=starting_range[0]
upper_bound=starting_range[1]
search_step=round((upper_bound-lower_bound)/100000)
print('Search step:', search_step)
for i in range(lower_bound, upper_bound, search_step):
  x=i
  locations.append((search_maps(maps[1:],x), i))

min_value=min(locations)
print('Better guess - final value and starting value:', min_value)

final_starting_point=min_value[1]
distance=10000

locations=[]
for i in range(final_starting_point-distance, final_starting_point + distance):
  x=i
  locations.append((search_maps(maps[1:],x), i))

min_value=min(locations)
print('\nSolution for part 2:', min_value[0])
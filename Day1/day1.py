import re
import numpy as np

def get_first_and_last_digit(line):
    #unpack string and get all numbers
    numbers=[char for char in [*line] if char.isdigit()]
    return int(numbers[0] + numbers[-1])

def get_values(fun, list_of_lists):
    #get max/min value and index of list using generator expression
    return fun((value,i) for i, row in enumerate(list_of_lists)
                         for j, value in enumerate(row))


with open('input.txt') as f:
  lines=[line.strip() for line in f.readlines()]

x=map(get_first_and_last_digit, lines)
print('Solution for part 1: ', np.sum(list(x)))

#------------------------------------------------
numbers=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

calibration_values_sum=0
for i,line in enumerate(lines):
  y=[]
  for i,number in enumerate(numbers):
    #each list represents one digit; values in lists are indices of numbers
    y.append([m.start() for m in re.finditer(number + '|' + str(i+1), line)])

  last_digit = get_values(max,y)[1]+1
  first_digit = get_values(min,y)[1]+1

  #print(y)
  calibration_values_sum+=first_digit*10+last_digit

print('Solution for part 2: ', calibration_values_sum)

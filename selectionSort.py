from random import seed
from random import randint
seed(1)
arr = []
temp = 0

def swap(list, x, y):
  list[x], list[y] = list[y], list[x]
  return list

for _ in range(5):
  value = randint(0, 99)
  arr.append(value)

for i in range(0, len(arr)):
  max = 0;
  for j in range(0, len(arr) - i):
    if (arr[max] < arr[j]):
      max = j
  swap(arr, max, j)
  print(arr)
  print(arr[max]);

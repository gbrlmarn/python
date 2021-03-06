import math

unit_den_array = [0]*10
iter = 0

def gcd(a, b):
  c = a%b
  while (c > 0):
    a = b
    b = c
    c = a % b
  return b


def decompose(num, den):
  global iter
  if(num == 1):
    iter = iter+1
    unit_den_array[iter] = den
  else:
    unit_den = math.ceil(den/num)
    iter = iter+1
    unit_den_array[iter] = unit_den
    gcd_of_numbers = gcd((num*unit_den) - den, den*unit_den)
    decompose(((num*unit_den) - den)//gcd_of_numbers, (den*unit_den)//gcd_of_numbers)

if __name__ == '__main__':
  decompose(21,23)
  for i in range(1, iter+1):
    print(unit_den_array[i])
 

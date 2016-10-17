def getResult(m,n):
  return get_even_power_sum(n // 2) * (m + 1)

def get_even_power_sum(max):
  sum = 0;
  d = 2;
  while d <= max:
    sum += max // d;
    d *= 2;
  return sum;

print(getResult(904961, 8));
print(getResult(904961, 10**12));
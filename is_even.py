
def is_even(x):
  return x % 2 == 0
print(is_even(5))

numbers = [1,56,234,87,4,76,24,69,90,135]  
print(filter(is_even,numbers))

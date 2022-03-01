list_x = [2, 4, 5, 5, 8, 9]
tuple_y = (2, 4, 5, 5, 8, 9)

#demostrating that tuple are immutable while lists are mutable
try:
  list_x.remove(2)	
  print('item succefully removed')
except:
  print("list are immutable")

try:
  tuple_y.remove(2)	
  print('item succefully removed')
except:
  print("tuples are immutable")
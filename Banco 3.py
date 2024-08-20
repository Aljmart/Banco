def funcion(l1):
  l1.sort()
  var = 0
  for i in l1:
      if i > var + 1:
          return var+ 1
      var += i
  return var+ 1
m=[5,7,1,1,2,3,22]
final=funcion(m)
print(final)
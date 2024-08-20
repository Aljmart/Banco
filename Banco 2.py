s=8
l1=[1,2,3,5,6,800,9,-2,-3,-5,-6,-8,-9,0,5.5,10]
def funcion(s,l1):
  ss=(s*10)+s
  final=[]
  for i in (l1):
    var=i**2
    if var<ss:
      final.append(var)
  for j in range(len(final)-1):
    for k in range(len(final)-j-1):
      if final[k]>final[k+1]:
        aux=final[k]
        final[k]=final[k+1]
        final[k+1]=aux
  return final
vectorfinal=funcion(s,l1)
print("el vecyor final es:",vectorfinal)
print("el vector original es:",l1)
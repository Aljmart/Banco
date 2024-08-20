s=8
l1=[10,20,3,40,50,89,76,39,60,61,7,46,74,100,8,90]
l2=[10,20,30,40]
i=0
fi=[]
prueba=[]
while i<len(l1):
  if l1[i] <s:
    fi.append(l1[i])
  u=l1[i]//10
  while u!=0:
    u2=l1[i]%10
    if u>=s:
      if u2<s:
        fi.append(u2)
    elif u2>=s:
      fi.append(u)
    else:
      fi.append(l1[i])
    u=u//10
  i+=1
print(fi)
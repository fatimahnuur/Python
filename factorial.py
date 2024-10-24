def fact(a):
  s=1
  if a==0 or a==1:
    s=1
  else:
    for i in range(1,a+1):
      s*=i
  return s

n=fact(3)
print(n)

 





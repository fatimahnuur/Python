kvadratt=lambda s: s**2
print(kvadratt(7))




print("##################")


num=[3,4,5,3,5,3,35554,8]

kvadrat=list(map(lambda n: n**2,num))
print(kvadrat)

print("##################")

enter=int(input('Ixtiyoriy sonni kiriting===>'))
royxat=list(range(enter))

juft=list(filter(lambda x:x%2==0,royxat))
print(juft)

print("##################")

juft=list(map(lambda x: f'juft son==> {x}' if x%2==0 else  f'toq son==>{x}' , royxat))
print(juft)






# 1. Bo'sh to'plam yarating va uni chop eting.
toplam = set()
print(toplam)

# 2. To'plamga uchta element qo'shing va chop eting.
my_set.update([1, 2, 3])
print(my_set)

# 3. To'plamga yangi element qo'shing va uni qayta chop eting.
my_set.add(4)
print(my_set)

# 4. Foydalanuvchidan 5 ta son so'rang va ularni to'plamga joylashtirib, chop eting.
for _ in range(5):
    num = int(input("Son kiriting: "))
    my_set.add(num)
print(my_set)

# 5. To'plamdagi elementlarni for tsikli yordamida chop eting.
for element in my_set:
    print(element)

# 6. To'plamdagi elementlar sonini chop eting.
print(f"To'plamdagi elementlar soni: {len(my_set)}")

# 7. To'plamdagi bir elementni o'chiring va qayta chop eting.
my_set.remove(1) 
print(my_set)

# 8. To'plamni boshqa to'plam bilan birlashtirib, yangi to'plam yarating va chop eting.
set_1 = {5, 6, 7}
set_2 = my_set.union(set_1)
print(set_2)

# 9. Ikkita to'plamni solishtirib, ularning kesishgan elementlarini chop eting.
intersection = my_set.intersection(set_1)
print(intersection)

# 10. To'plamdan elementni tasodifiy tarzda olib tashlang va to'plamni qayta chop eting.
my_set.pop()
print(my_set)

# 11. To'plamdagi barcha elementlarni alifbo tartibida chop eting.
sorted_set = sorted(my_set)
print(sort_set)

# 12. To'plamni boshqa to'plamdan farqli elementlarini chop eting.
difference = my_set.difference(other_set)
print(difference)

# 13. To'plamda mavjud bo'lgan elementlarni for tsikli bilan chop eting.
for element in my_set:
    print(element)

# 14. To'plamdagi barcha elementlarni teskari tartibda chop eting.
reversed_set = sorted(my_set, reverse=True)
print(reversed_set)

# 15. To'plamni tozalang va bo'sh to'plamni chop eting.
my_set.clear()
print(my_set)















  

   

  








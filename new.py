ism='ali vali salim akbar sadoqat fotima'

ismlar=ism.split()

katta_harf=lambda ism: ism.capitalize()
natija=list(map(katta_harf, ismlar))

print(natija)

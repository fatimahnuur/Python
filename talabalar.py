ismlar='Murodil Sadoqat Sarvinoz Fotima Jasurbek Javlon'
talabalar=ismlar.split()
talabalar

talaba=input('Talaba ismini kiriting: ').capitalize

if talaba in talabalar:
    print(f'{talaba} bugun darsda')
else:
    print(f'{talaba} darsga kelmagan')
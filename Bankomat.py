class Bankomat:
    def __init__(self, name, num, cash, code):
        self.name = name
        self.num = num
        self.cash = cash
        self.code = code

    def balans(self):  # Balansni bilish
        print(f"Balans {self.name} kartangizda {self.cash} so'm")

    def deposit(self, naqd):  # Pul o'tkazish
        if naqd > 1000:
            self.cash += naqd
            print(f'Kartangizga {naqd} so\'m o\'tkazildi. Balans {self.cash} so\'m')
        else:
            print('Iltimos yetarli miqdorda pul kiriting. Minimal 1000 so\'m')

    def withdraw(self, naqd):  # Naqd pul yechish
        if naqd > 0 and naqd <= self.cash:
            self.cash -= naqd
            print(f'Kartangizdan {naqd} so\'m pul yechib olindi. Balans {self.cash} so\'m')
        else:
            print('Yetarli mablag\' yo\'q yoki noto\'g\'ri miqdor.')

    def pin(self, parol): 
        if parol == self.code:
            print('Qaysi amalni bajarmoqchisiz?:')
        else:
            print('Parol noto\'g\'ri kiritilgan, Iltimos qaytadan urinib ko\'ring.')


###########################################################################

karta = Bankomat('Humo', '1234 5678 9012 3456', 1000000, 2323)  # Saqlangan karta

check_pin = int(input('Pin code ni kiriting==> '))
karta.pin(check_pin)  # Pass the entered PIN

amal = input('Qaysi buyruqni amalga oshirmoqchisiz? ==>\nBalans \nDeposit \nWithdraw \nAmalni kiriting: ').capitalize()

if amal == 'Balans':
    karta.balans()

elif amal == 'Deposit':
    miqdor = int(input('O\'tkazma miqdorini kiriting(minimal 1000 so\'m==>) '))
    karta.deposit(miqdor)

elif amal == 'Withdraw':
    miqdor = int(input('Pul miqdorini kiriting(minimal 1000 so\'m==>) '))
    karta.withdraw(miqdor)

else:
    print('Amallar xato kiritilgan, iltimos qaytadan urinib ko\'ring')













     



      
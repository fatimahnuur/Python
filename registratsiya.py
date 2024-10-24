#Isaqova Fotimaxon 15.10.2024 12:24 :) Yangilandi: 15:12:2024 numberga isdigit() qo'shildi

#Registratsiya
start = input('Ro\'yxatdan o\'tishni xohlaysizmi?==> ').lower()

if start == 'ha':
    while True:  
        login = input('Loginni kiriting: ')   #login
        email = input('Email pochtangizni kiriting: ') #elektron pochta
        number = input('Telefon raqamingizni kiriting: +998 ') #telefon raqam
        password = input('Parolni kiriting:') #parol 

        if len(login) >= 8 and login.isalpha(): #agar login uzunligi 8 yoki 8 dan ko'p bo'lsa va loginda harflar bo'lsa,
            if email.endswith('@gmail.com') and (len(number) == 9 and number.isdigit()): # kiritilgan email oxiri "@gmail.com" bilan tugasa va va number uzunligi 9 ga teng bo'lsa va raqamlardan tashkil topsa. 
                if len(password) >= 8 and password != "12345678": #parol uzunligi 8 yoki 8 dan ko'p bo'lsa va parol "12345678" bilan boshlanmasa,
                    print('Siz ro\'yxatdan o\'tdingiz!') #tabriklaymiz siz ro'yxatdan o'tdingiz
                    # login va parolni saqlab qoyamiz.
                    cloud_login = login
                    cloud_password = password
                    break  
                else: 
                    print('Parol 8 tadan ko\'p belgidan iborat bo\'lishi kerak va "12345678" emas.')
            else:
                print('Raqam yoki elektron pochta xato kiritilgan.')
        else:
            print('Login 8 ta harfdan iborat bo\'lishi kerak.')


# Login
kirish = input('Loginni kiriting: ')
parol = input('Parolni kiriting: ')

if cloud_login and cloud_password: #agar ro'yxatdan o'tgan bo'lsa
    if kirish==cloud_login and parol==cloud_password: # parol va login to'g'ri kelsa,
        print('Siz akkountingizga kirdingiz.') #akkountga kirildi
    else:
       print('Parol yoki login xato, iltimos qaytadan urinib ko\'ring.')
else:
    print('Siz ro\'yxatdan o\'tmagansiz.')


    




    


    
     

     



  


    
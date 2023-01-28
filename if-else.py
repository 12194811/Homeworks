# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:05:04 2023

@author: GOFURJON
"""

#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for avto in cars:
    if avto == "gm":
        print(avto.upper())
    else:
        print(avto.title())
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for avto in cars:
    if avto != "gm":
        print(avto.upper())
    else:
        print(avto.title())
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
ism = input("login ismingiz nima?\n>>>")
if ism == 'admin':
    print(f"Xush kelibsiz, {ism.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?" )
else:
    print("Xush kelibsiz", ism)
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.    
x = float(input("Birinchi son kiriting: "))
y = float (input("Ikkinchi son kiriting: "))
if x == y:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")
#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
x = float(input("Istalgan son kiriting: "))
if x<0:
    print("Manfiy son")
else:
    print("Musbat son")
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
x = float(input("Son kiriting: "))
if x >0:
    print(x**1/2)
else:
    print("Musbat son kiriting:")
    

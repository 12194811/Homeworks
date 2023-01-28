# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 01:53:32 2023

@author: GOFURJON
"""

#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Abdulloh', 'Abdurrohman', 'Abdulgaffor', 'Abdurrashid', 'Abdulgani']
for abdga in ismlar:
    print(f"Birodarim {abdga}, sizga Allohning rahmati bolsin.")
#Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
miqdor = ("Kod 5 martta takrorlandi.")
print(miqdor)    
#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
toq_sonlar = list(range(11,100,2))
for kub in toq_sonlar:
    print(f"{kub} ning kubi {kub**3} ga teng.")
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("5 ta eng sevimli kinoyingiz nomini kiriting:")
for k in range(5):
    kinolar.append(input(f"{k+1} - kinoning nomini kiriting: "))
print(kinolar)
#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
odamlar = []
print("Bugun nechta odam bilan suhbatlashdingiz?")
for o in range(5):
    odamlar.append(input(f"{o+1} - siz suhbatlashgan odamning ismi: "))
print(odamlar)
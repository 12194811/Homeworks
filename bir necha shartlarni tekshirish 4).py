# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:22:34 2023

@author: GOFURJON
"""

#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
mahsulotlar = ['kartoshka', 'gosht', 'guruch', 'yog', 'non', 'sabzi', 'piyoz', 'makaron', 'choy', 'tuxum']
savat = []
for n in range(5):
    savat.append(input(f"Olmoqchi bolgan {n+1}- mahsulot nomini kiriting: "))
    
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")
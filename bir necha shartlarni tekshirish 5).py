# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:46:34 2023

@author: GOFURJON
"""

#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
mahsulotlar = ['kartoshka', 'gosht', 'guruch', 'yog', 'non', 'sabzi', 'piyoz', 'makaron', 'choy', 'tuxum']
savat = []
for n in range(5):
   savat.append(input(f"Olmoqchi bolgan {n+1}- mahsulot nomini kiriting: "))

bor_mahsulotlar = []
mavjud_emas = []    
for m in savat:
    if m in mahsulotlar:
        bor_mahsulotlar.append(m)
    else:
        mavjud_emas.append(m)
        
if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
        

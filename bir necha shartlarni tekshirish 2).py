# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:53:11 2023

@author: GOFURJON
"""

#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
yosh = int(input("Yoshingiz nechida? "))
if yosh<=4 or yosh>=60:
    price = 0
elif yosh<=18:
    price = 10000
else:
    price = 20000    
print(f"Sizga kirish {price} so'm")
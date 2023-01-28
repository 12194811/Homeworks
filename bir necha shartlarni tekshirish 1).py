# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:45:24 2023

@author: GOFURJON
"""

#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
juft_son = float(input("Juft son kiriting: "))
if juft_son % 2:
    print("Bu son juft emas.")
else:
    print("Rahmat.")
    
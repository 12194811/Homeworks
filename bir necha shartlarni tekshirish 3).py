# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:16:46 2023

@author: GOFURJON
"""

#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring.
son = float(input("Birinchi sonni kiriting: "))
son_ = float(input("Ikkinchi sonni kiriting: "))
if son >= son_:
    print("Birinchi son katta")
else:
    print("Ikkinchi son katta")
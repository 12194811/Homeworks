# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:18:28 2023

@author: GOFURJON
"""

#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
foydalanuvchilar = ['ali', 'vali', 'anvar', 'hasan', 'husan']
login = []
login.append(input("Login kiriting: "))
    
for m in login:
    if m in foydalanuvchilar:
        print("Login band, yangi login tanlang!")
    else:
        print("Xush kelibsiz, foydalanuvchi!")
        
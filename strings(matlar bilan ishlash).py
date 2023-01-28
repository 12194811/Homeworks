# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 23:47:26 2023

@author: GOFURJON
"""
# Quyidagi o'zgaruvchilarni yarating:
#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"
#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
#Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
ism = input("Kochaning nomi?")
print(ism)
ism = input("Mahallaning nomi?")
print(ism)
ism = input("Tumanning nomi?")
print(ism)
ism = input("Viloyatning nomi?")
print(ism)
viloyat="Samarqand"
print(f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print("Bog'bon kochasi,\nSog'bon mahallasi, \nBodomzor tumani, \nSamarqand viloyati.")
#Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
yangi_kocha="Bog'bon"
yangi_mahalla="Sog'bon"
yangi_tuman="Bodomzor"
yangi_viloyat="Samarqand"
print(f"{yangi_kocha.title()}, {yangi_mahalla.upper()}, {yangi_tuman.lower()}, {yangi_viloyat.capitalize()}")
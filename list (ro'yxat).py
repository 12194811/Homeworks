# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 22:43:24 2023

@author: GOFURJON
"""
#Quyidagi mashqlarni bajaring:
#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
ismlar = ['Abdulloh', 'Abdurrohman', 'Muhammad']
print("Assalamu alaykum,", ismlar[0], "bugun istig'for aytdingmi?")
print(ismlar[1], "salovat aytishni unutmadingmi?")
print(ismlar[2], "(sallallohu alayhi vasallam)")
#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [23,-6784,75346,239.458]
#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
sonlar = [23,-6784,75346,239.458]
print(sonlar[3]-sonlar[1], sonlar[0]/sonlar[2])
# ikkinchi variant
sonlar = [23,-6784,75346,239.458]
sonlar[0]=5769458
sonlar[2]=2950
sonlar[3]=sonlar[1]+sonlar[0]
print(sonlar)
#t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ['Muhammad (s.a.v)', 'Abu Bakr(r.a)', 'Umar ibn Xattob', 'Usmon ibn Afvon', 'Ali ibn Abu Tolib']
z_shaxslar = ['Muhammadali', 'Abdulloh', 'Abdukarim', 'Zokirjon', 'Oybek']
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
birinchi = t_shaxslar.pop(0)
ikkinchi = z_shaxslar.pop(3)
print("Men", birinchi, "ni tushda ko'rishni xohlayman.")
print(ikkinchi, "- juda hikmatga boy inson.")
#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append("Zakariyo")
friends.append("Dovud")
friends.append("Ilyas")
friends.append("Idris")
friends.append("Ubay ibn Kaab")
friends.append("Muoz ibn Jabal")
print(friends)
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove("Dovud")
friends.remove("Ilyas")
print(friends)
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0, 'Asadulloh')
friends.insert(2, 'Umar')
friends.insert(3, 'Ali')
print(friends)
#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = [friends.pop(1), friends.pop(3), friends.pop()]
print(mehmonlar)
mehmonlar.append("Abdurrahmon")
print(mehmonlar)
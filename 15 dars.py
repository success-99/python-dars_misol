poytaxtlar={
"uzbekiston":"tashkent",
"russia":"moscov",
"italiya":"rim",
"angliya":"london",
"germaniya":"berlin",
"saudiya arabistoni":"ar-riyod"
}

#  "< bilet bor yoqligini aniqlovchi datur >".



b_poytaxtlar=[]
bor_p=[]
yoq_p=[]
y=int(input(f"\nNechta Poytaxtga bormoqchisiz? > "))
for d in range(y):
    b_poytaxtlar.append(input(f"{d+1} - "))
for t in b_poytaxtlar:
    if t in poytaxtlar.values():
        bor_p.append(t.title())
       # print(f" Bor {t}")
    else:
        yoq_p.append(t.title())
        
print("Bileti mavjud bo'lgan Poytaxtlar: ")
for i in bor_p:
    print(i)
print("Bileti tugagan Poytaxtlar: ")
for g in yoq_p:
    print(g)
   

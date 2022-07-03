# cars={"model":"BMW", "narx":"40000$", "yili":"2021", "davlat":"Germaniya"}
# print(f"{cars['model'].lower()}")
# cars['rangi']='oq'
# cars["rangi"]="qora"
# del cars["yili"]
# print(cars)
# /////////////////////////////////////********************
# poytaxtlar={
# "uzbekiston":"tashkent",
# "russia":"moscov",
# "italiya":"rim",
# "angliya":"london",
# "germaniya":"berlin",
# "saudiya arabistoni":"ar-riyod"
# }
# /////////////////////////////////////********************

# poytaxt = poytaxtlar.get("saudiya arabistoni", "Bu poytaxt lug'atda yo'q")
# print(poytaxt.title())

# print([poytaxtlar.items()])

# ////////////////////////////////////////

# for k, q in poytaxtlar.items():
#     print(f" \nDavlat > {k.title()},  Poytaxt > {q.title()}\n")
# ////////////////////////////////////////
# print(poytaxtlar.keys())

# for m in poytaxtlar.keys():
#     print(f"{m.title() } ")


# for m in poytaxtlar.values():
#     print(f"   {m.title() }") 
# ///////////////////////////////////////////////
# "tashkent", "qohira", "vashington", "ar-riyod"
# //////////////////////////////////////////////////////////*******************
# "< bilet bor yoqligini aniqlovchi datur >"
# b_poytaxtlar=[]
# bor_p=[]
# yoq_p=[]
# y=int(input(f"\nNechta Poytaxtga bormoqchisiz? > "))
# for d in range(y):
#     b_poytaxtlar.append(input(f"{d+1} - "))
# for t in b_poytaxtlar:
#     if t in poytaxtlar.values():
#         bor_p.append(t.title())
#         # print(f" Bor {t}")
#     else:
#         yoq_p.append(t.title())
#         # print(f"Yo'q {t}")
# print("Bileti mavjud bo'lgan Poytaxtlar: ")
# for i in bor_p:
#     print(i)
# print("Bileti tugagan Poytaxtlar: ")
# for g in yoq_p:
#     print(g)

    # -/////////////////////////////////////////////*****************


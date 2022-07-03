# m_shaxslar={
#     "Abu Abdulloh Muhammad ibn Ismoil":{
#         "asarlari":["al-jome' as-sahih","al-adab al-mufrad","at-tarix al-kabir","at-tarix as-sag'ir"]},
#     "Abdulla Qodiriy":{
#         "asarlari":["o'tkan kunlar", "mehrobdan chayon", "obid ketmon"]},
#     "Alisher Navoiy":{
#         "asarlari":["xams", "lison ut-tayr", "mahbub al-qulub", "munojot"]
#     }

# }

# for shaxs,asar in m_shaxslar.items():
#     print(f"{shaxs}ning kitoblari")
#     for t in asar["asarlari"]:
        
#         if t =="xams":
#             print("Xamsa")
#         else:
#             print(t.capitalize())

# //////////////////////////////////////////////////

# import turtle
# turtle.bgcolor("black")
# turtle.speed(0)
# turtle.hideturtle()

# colors=["green", "red", "green"]
# for u in range(120):
#     for d in colors:
#         turtle.color(u)
#         turtle.circle(200-u, 100)
#         turtle.lt(90)
#         turtle.circle(200-u, 100)
#         turtle.rt(60)
#         turtle.end_fill()
# turtle.mainloop()
# //////////////////////////////////////////////////
# avftolar=[]
# for t in range(5):
#     car={
#         "modeli":"cobalt",
#         "rangi":"None",
#         "yili":"2021",
#         "narxi":"None",
#         "karobka":"avto"
#     }
#     avftolar.append(car)
# for c in avftolar[:2]:
#     c["narxi"]="14000$"
#     c["rangi"]="qora"
#     c["modeli"]="jentra"
# for c in avftolar[2:]:
#     c["rangi"]="oq"
#     c["narxi"]="13000$"

 

 

# for y in avftolar:
#     print(y)    


# o_car=[]
# for y in range(3):
#     o_car.append(input(f"{y+1} - mashina nomini kiriting: "))
# print(o_car)

# for h in o_car:
#     if h in car["modeli"]:
#         print("bor")
#     else:
#         print("yoq")
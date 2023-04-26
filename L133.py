# Olivia Busk, Bethany Berlage, Grace Anspach

import dbm

db1=dbm.open("captions","c")
# db1["Hello.jpeg"]="Hey, hi, hello"
# db1["Goodbye.jpeg"]="goobye, see ya, peace out"
# db1["Names.jpeg"]="Olivia, Bethany, Grace"
# db1["Food.jpeg"]="banana, cookie, cake"
# db1["Flowers.jpeg"]="daisy, rose, lily"

# print(db1["Hello.jpeg"])
# print(db1["Goodbye.jpeg"])
# print(db1["Names.jpeg"])
# print(db1["Food.jpeg"])
# print(db1["Flowers.jpeg"])

for item in db1:
    print(item, db1[item])

db1.close()

import random

#ein sternchenn generattor setzt an jedes ende vom wort ein stern ⭐ 
#beispiel: ⭐hallo⭐ ⭐nico⭐

import random


emojis = ("⭐ ", "🍕 ", "🧁 ", "🥝 ")

user = input(">> ")

randomitem = random.choice(emojis)

transform = user.split(" ")

x = randomitem.join(transform)

print(x)

#in ein wort zusammenfügen, damit es aussieht wie: ⭐hallo⭐
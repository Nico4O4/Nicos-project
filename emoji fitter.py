import random


emojis = ("⭐ ", "🍕 ", "🧁 ", "🥝 ")

user = input(">> ")

randomitem = random.choice(emojis)

transform = user.split(" ")

x = randomitem.join(transform)

print(x)
#coded by nico4o4
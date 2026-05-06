animeNames = ["spy x family", "Lycoris", "Bocchi the Rock", "Komi", "Fragrant flower", "Frieren"]

for names in animeNames:
    count_characters = len(names)   #len = lenght - zählt die länge eines strings
    count_free_space = names.count(" ")  #count zählt einen spezifischen substring un gibt anzahl zurück
    
    print(names, " | Total String Characters: ", count_characters, "| Space: ", count_free_space)

count_whole_names = len(animeNames)
print("All animes: ", count_whole_names)
        

#Made by: Nico4O4
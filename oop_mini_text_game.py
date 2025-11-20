class items:
    def __init__(def_selbst_aka_self, atares_poition, atares_sword):
        def_selbst_aka_self.poition = atares_poition
        def_selbst_aka_self.sword = atares_sword

obj0 = items("Atares Potion", "Atares Sword")



class items_wert:
    def __init__(def_selbst, normal, defiant, eleksant):
        def_selbst.normal = normal                         
        def_selbst.defiant = defiant
        def_selbst.eleksant = eleksant

obj = items_wert(35, 45, 60)                                                    #immer Objekt zuerst wählen dann atribute aka. werte hinzufügen



class Player_stats:
    def __init__(self, health_var, strenght_var, play_time_var):
        self.health = health_var
        self.strenght = strenght_var
        self.play_time = play_time_var

obj1 = Player_stats(100, 110, 25)





print("\n\n---Inventory---\n\n")
print(f"Items:\n {obj0.poition} / Value {obj.normal}\n {obj0.sword} / Value {obj.defiant}")


print("\n\n---Player Stats--\n\n")
print(f"Health / {obj1.health}\n Strenght / {obj1.strenght}\n Play Time / {obj1.play_time}")

#coded by: Nico4O4
#-Absolute Cinema-
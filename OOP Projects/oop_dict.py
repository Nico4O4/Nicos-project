class  Myclass:
    def __init__(self, save, show):

        fav_animes = {
        "name": self.answer_var 
        }

        self.answer_var = save #answer_var wo es tatsächlich gespeichert wird
        self.show_var = show


        self.answer_var["name"] = self.answer_var
        
        self.show_var = fav_animes.get("name")

        #printen
        print("Your answer: ", self.show_var)
        
user_input = Myclass(input("Whats your fav anime? "))




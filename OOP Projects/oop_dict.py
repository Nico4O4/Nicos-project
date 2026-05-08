class  Myclass:
    def __init__(self, user_input_taker, sec_input_taker):
        #self.irgendwas (irgendwas) ist die variable mit der tatsächlichen info

        self.take_input = user_input_taker
        self.take_input = None

        if self.take_input is False:
            self.take_sec_input = sec_input_taker

    
        animes =  {"absolute_fav_anime": self.take_input, "second_fav_anime": self.take_sec_input}   
        
        
        print(animes)

def menu():
    user_input = Myclass(input("Answer "))
    user_input1 = Myclass(input("Answer "))



if __name__ == "__main__":
    menu()

#--notes--
#p1 = Person("Linus", 28) - linus die erste variable in der class 28 die zweite variable man fügt das nacheinander ein
#irgendwie den nächsten input in die nächste var speichern aber wie???

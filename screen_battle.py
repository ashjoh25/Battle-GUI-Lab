import tkinter

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        self.player1 = player1
        self.player2 = player2

        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        self.char_choice = tkinter.Button(self, text = "Attack!", fg = 'red', bg = 'black', command = self.attack_clicked, font=('Centaur'))
        self.char_choice.grid(row = 0, column = 1)
        tkinter.Label(self, text = "You", font=('Centaur')).grid(row = 3, column = 1, sticky = tkinter.E + tkinter.W)
        tkinter.Label(self, text = "Computer", font=('Centaur')).grid(row = 3, column = 2, sticky = tkinter.E + tkinter.W)

        self.imageSmall = tkinter.PhotoImage(file="images/" + self.player1.small_image)
        self.w = tkinter.Label(self, image = self.imageSmall)
        self.w.grid(row = 4, column = 1)
        self.w.photo = self.imageSmall
        self.imageSmall = tkinter.PhotoImage(file="images/" + self.player2.small_image)
        self.w = tkinter.Label(self, image = self.imageSmall)
        self.w.grid(row = 4, column = 2)
        self.w.photo = self.imageSmall

        self.p1hp = self.player1.hit_points
        self.p2hp = self.player2.hit_points

        self.person_hit_points = tkinter.Label(self, text = f"{self.player1.hit_points}/{self.p1hp} HP", font=('Centaur'))
        self.person_hit_points.grid(row = 5, column = 1, sticky = tkinter.E + tkinter.W)
        self.computer_hit_points = tkinter.Label(self, text = f"{self.p2hp}/{self.player2.hit_points} HP", font=('Centaur'))
        self.computer_hit_points.grid(row = 5, column = 2, sticky = tkinter.E + tkinter.W)

        self.person_attack = tkinter.Label(self, text = "", font = ('Centaur', 11))
        self.person_attack.grid(row = 0, column = 2)
        self.computer_attack = tkinter.Label(self, text = "", font = ('Centaur', 11))
        self.computer_attack.grid(row = 1, column = 2)

    def attack_clicked(self):
        self.person_attack["text"] = self.player1.attack(self.player2)
        self.computer_attack["text"] = self.player2.attack(self.player1)

        self.person_hit_points["text"] = f"{self.player1.hit_points}/{self.p1hp} HP"
        self.computer_hit_points["text"] = f"{self.player2.hit_points}/{self.p2hp} HP"

        if self.player1.hit_points <= 0 or self.player2.hit_points <= 0:
            if self.player1.hit_points <= 0:
                self.winner = tkinter.Label(self, text = f"{self.player2.name} is victorious!", font = ('Centaur', 11))
                self.winner.grid(row = 2, column = 2)
            elif self.player2.hit_points <= 0:
                self.winner = tkinter.Label(self, text = f"{self.player1.name} is victorious!", font = ('Centaur', 11))
                self.winner.grid(row = 2, column = 2)
            self.char_choice.destroy()
            self.exit = tkinter.Button(self, text = "Exit", command = self.exit_clicked, fg = 'red', bg = 'black', font = ('Centaur')).grid(row = 6, column = 2)
                                            
    def exit_clicked(self):     
        self.callback_on_exit()
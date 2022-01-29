import tkinter

class Screen_PrepareToBattle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        self.player1 = player1
        self.player2 = player2

        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()

    
    def create_widgets(self):
        tkinter.Label(self, text = "You", font=('Centaur')).grid(row = 0, column = 0, sticky = tkinter.E + tkinter.W)
        tkinter.Label(self, text = "Computer", font=('Centaur')).grid(row = 0, column = 1, sticky = tkinter.E + tkinter.W)
        tkinter.Label(self, text = f"{self.player1.hit_points} HP", font=('Centaur')).grid(row = 2, column = 0, sticky = tkinter.E + tkinter.W)
        tkinter.Label(self, text = f"{self.player1.dexterity} Dexterity", font=('Centaur')).grid(row = 3, column = 0, sticky = tkinter.E + tkinter.W)
        tkinter.Label(self, text = f"{self.player1.strength} Strength", font=('Centaur')).grid(row = 4, column = 0, sticky = tkinter.E + tkinter.W)
        tkinter.Label(self, text = f"{self.player2.hit_points} HP", font=('Centaur')).grid(row = 2, column = 1, sticky = tkinter.E + tkinter.W)
        tkinter.Label(self, text = f"{self.player2.dexterity} Dexterity", font=('Centaur')).grid(row = 3, column = 1, sticky = tkinter.E + tkinter.W)
        tkinter.Label(self, text = f"{self.player2.strength} Strength", font=('Centaur')).grid(row = 4, column = 1, sticky = tkinter.E + tkinter.W)

        self.imageSmall = tkinter.PhotoImage(file="images/" + self.player1.small_image)
        self.w = tkinter.Label(self, image = self.imageSmall)
        self.w.grid(row = 1, column = 0)
        self.w.photo = self.imageSmall
        self.imageSmall = tkinter.PhotoImage(file="images/" + self.player2.small_image)
        self.w = tkinter.Label(self, image = self.imageSmall)
        self.w.grid(row = 1, column = 1)
        self.w.photo = self.imageSmall

        self.char_choice = tkinter.Button(self, text = "Commence Battle!", fg = 'red', bg = 'black', command = self.commence_battle_clicked, font=('Centaur')).grid(row = 5, column = 1)


    def commence_battle_clicked(self):        
        self.callback_on_commence_battle()
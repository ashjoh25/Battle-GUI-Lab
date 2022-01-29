import tkinter

class Screen_CharacterSelection (tkinter.Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
        self.roster = roster
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        self.character_index = tkinter.StringVar()
        self.character_index.set(None)
        
        tkinter.Label(self, text = "Hit Points", font=('Centaur')).grid(row = 0, column = 2, sticky = tkinter.E + tkinter.W)
        tkinter.Label(self, text = "Dexterity", font=('Centaur')).grid(row = 0, column = 3, sticky = tkinter.E + tkinter.W)
        tkinter.Label(self, text = "Strength", font=('Centaur')).grid(row = 0, column = 4, sticky = tkinter.E + tkinter.W)
        row = 1
        for index in range(len(self.roster.character_list)):
            char = self.roster.character_list[index]
            tkinter.Radiobutton(self, text = char.name, font=('Centaur'), variable = self.character_index, value = index).grid(row = row, column = 0, sticky = tkinter.W)
            tkinter.Label(self, text = char.hit_points, font=('Centaur')).grid(row = row, column = 2, sticky = tkinter.E + tkinter.W)
            tkinter.Label(self, text = char.dexterity, font=('Centaur')).grid(row = row, column = 3, sticky = tkinter.E + tkinter.W)
            tkinter.Label(self, text = char.strength, font=('Centaur')).grid(row = row, column = 4, sticky = tkinter.E + tkinter.W)
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image)
            w = tkinter.Label(self, image = imageSmall)
            w.grid(row = row, column = 1)
            w.photo = imageSmall
            row += 1
        
        self.char_choice = tkinter.Button(self, text = "Character Selected!", fg = 'red', bg = 'black', command = self.selected_clicked, font=('Centaur')).grid(row = row, column = 3)
 
    def selected_clicked(self):
        self.callback_on_selected(self.character_index.get())
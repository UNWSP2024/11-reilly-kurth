#reilly Kurth
#program 1 wk11
#4/9/2025

import tkinter

class Saying:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Favorite Saying")
        self.label = tkinter.Label(self.main_window, text="When life gives you lemons, make lemonade")
        self.label.pack()
        self.main_window.mainloop()

if __name__ == '__main__':
    saying = Saying()


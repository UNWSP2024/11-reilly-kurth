#reilly Kurth
#4/11/2025
#Program #2
import tkinter
import tkinter.messagebox

class AddressGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Information")
        self.display_button = tkinter.Button(self.main_window, text="Display Information", command=self.display_address)

        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.display_button.pack(ipadx=3, ipady=3, padx=10, pady=10)
        self.quit_button.pack(ipadx=3, ipady=3, padx=10, pady=10)
        self.main_window.mainloop()
    def display_address(self):
        tkinter.messagebox.showinfo("Information", "Reilly Kurth\nAddress")

if __name__ == '__main__':
    addressGUI = AddressGUI()
from tkinter import Tk
from Splash_screen import make_splash_screen

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def kill_all_children(venster):
    for widget in venster.winfo_children():
        widget.destroy()

def main():
    root = Tk()
    root.geometry("1920x1080")
    root.title("Boromir")
    make_splash_screen(root)

    root.mainloop()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

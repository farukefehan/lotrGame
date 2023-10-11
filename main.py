from tkinter import Tk
from Splash_screen import make_splash_screen


def kill_all_children(venster):
    for widget in venster.winfo_children():
        widget.destroy()


def main():
    root = Tk()
    root.geometry("1920x1080")
    root.title("Boromir")
    make_splash_screen(root)

    root.mainloop()

if __name__ == '__main__':
    main()

import tkinter as tk
# from tkinter import Label, Frame
from PIL import Image, ImageTk

def loading_screen():
    image = Image.open("images/tolkien_estate_nieuw_fixed.png")

    root = tk.Tk()
    root.geometry("500x500")

    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1,)



    root.after(2500, root.destroy)

    root.mainloop()






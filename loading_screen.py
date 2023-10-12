import tkinter.font
from tkinter import Label, Tk
from PIL import Image, ImageTk

def loading_screen():
    image = Image.open("images/tolkien_estate_nieuw_fixed.png")
    image2 = Image.open("images/boromir7.png")
    resized_image = image2.resize(
        (600, 350), Image.LANCZOS)

    root = Tk()
    root.geometry("800x800")
    root.state('zoomed')

    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.place(x=0, y=0, relwidth=0.6, relheight=0.9)

    photo2 = ImageTk.PhotoImage(resized_image)

    label2 = Label(root, image=photo2)
    label2.place(relx=0.45, rely=0.2)

    text_font = tkinter.font.Font(family="Times", size=30, weight="bold")

    text_label = Label(text="TOLKIEN ESTATE\nBOROMIR DEV TEAM", font=text_font)
    text_label.place(relx=0.5, rely=0.8, anchor="center")

    root.after(2500, root.destroy)

    root.mainloop()






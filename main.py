from tkinter import Tk, Label
from Splash_screen import make_splash_screen
from paths_screen import generate_screen
from PIL import Image, ImageTk


def kill_all_children(venster):
    for widget in venster.winfo_children():
        widget.destroy()
    generate_background(venster)

def generate_background(root):
    original_image = Image.open(r"Images/background.png")
    resized_image = original_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(resized_image)
    background = Label(root, image=background_image)
    background.image = background_image
    background.place(x=0, y=0)

def main():
    root = Tk()
    root.geometry("1920x1080")
    root.title("Boromir")
    root.state('zoomed')


    option1_dict = {
        "text": "Option 1 tekst",
        "action": "action_code here"
    }
    option2_dict = {
        "text": "Option 2 tekst",
        "action": "action_code here"
    }
    option3_dict = {
        "text": "Option 3 tekst",
        "action": "action_code here"
    }
    option4_dict = {
        "text": "Option 4 tekst\n and more",
        "action": "action_code here"
    }

    options_list = [option4_dict, option3_dict, option2_dict, option1_dict]

    screen_dict = {
        "question": "put question here",
        "options": options_list
    }
    root.winfo_screenheight()
    root.winfo_height()
    generate_background(root)
    make_splash_screen(root)

    root.mainloop()

if __name__ == '__main__':
    main()

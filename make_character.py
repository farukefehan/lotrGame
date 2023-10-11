import tkinter as tk
from tkinter import Label
from tkinter.tix import Tk
from tkinter.ttk import Button, Entry

from PIL import ImageTk

characters =[]

def load_characters(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            characters_list ={
                "name": parts[0],
                "race": parts[1]
            }

            characters.append(characters_list)



def menu():
    root = tk.Tk()
    root.title("Character menu")
    root.geometry("400x300")
    img = ImageTk.PhotoImage(file="img.png")
    logo_frame = tk.Label(image= img)
    logo_frame.pack()
    Label(root, text="Main Menu").pack()
    Button(root, text="Create Character", command=create_character).pack()
    Button(root, text="Select Character", command=select_character).pack()
    root.mainloop()
def create_character():
    root = Tk()
    root.title("Create menu")
    root.geometry("400x300")
    Label(root, text="Enter character name:").pack()
    user_character_input = Entry(root)
    user_character_input.pack()
    Label(root, text="Enter character race:").pack()
    user_race_input = Entry(root)
    user_race_input.pack()
    Button(root, text="Save", command=lambda: save_character(user_character_input.get(), user_race_input.get())).pack()
    root.mainloop()
def save_character(name, race):
    characters.append({"name": name, "race": race})
    print("Character successfully created!")
def select_character():



def run():
    file_path = "characters.txt"
    load_characters(file_path)
    menu()

if __name__ == '__main__':
    run()
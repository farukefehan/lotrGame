import tkinter as tk
from tkinter.ttk import Label

from PIL import Image, ImageTk

characters = []

def load_characters_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                character_dict = {
                    "name": parts[0].strip(),
                    "race": parts[1].strip()
                }
                characters.append(character_dict)
            else:
                print(f"Invalid line: {line}")


def show_main_menu(venster):
    from main import kill_all_children
    kill_all_children(venster)

    tk.Label(venster, text="Main Menu").pack()
    tk.Button(venster, text="Create Character", command=customize_character).pack()
    tk.Button(venster, text="Select Character", command=select_character).pack()


def customize_character():
    customize_window = tk.Toplevel()
    customize_window.title("Character Customization")

    tk.Label(customize_window, text="Enter character name:").pack()
    name_entry = tk.Entry(customize_window)
    name_entry.pack()

    tk.Label(customize_window, text="Enter character race:").pack()
    race_entry = tk.Entry(customize_window)
    race_entry.pack()

    tk.Button(customize_window, text="Save", command=lambda: save_character(name_entry.get(), race_entry.get(), venster)).pack()

def save_character(name, race, venster):
    characters.append({"name": name, "race": race})
    tk.Label(venster, text="").pack()
    # print("Character successfully customized!")

def select_character():
    select_window = tk.Toplevel()
    select_window.title("Select Character")
    title = Label(select_window, text="Available characters:").pack()

    for i in range(len(characters)):
        character = characters[i]
        tk.Label(select_window, text=f"{i + 1}. {character['name']} - {character['race']}").pack()

    select_button = tk.Button(select_window, text="Select", command=on_character_selected)
    select_button.pack()

def on_character_selected():
    selected_index = int(input("Enter the number of the character you want to select: ")) - 1
    selected_character = characters[selected_index]
    print(f"Character '{selected_character['name']}' selected!")

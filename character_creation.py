from tkinter import Label, Entry, Button, StringVar, Tk, ttk
from PIL import Image, ImageTk

from character_selection import goto_adventure_selection_screen
from main import kill_all_children

races = ["Hobbit", "Elf", "Dwarf", "Human", "Wizard"]

class CharacterCreationScreen:
    current_race_index = 0
    character_dropdown = None

    @staticmethod
    def load_characters_from_file(file_path):
        characters = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    characters.append((parts[0], parts[1]))
        except FileNotFoundError:
            pass
        return characters

    @staticmethod
    def create_character_screen(venster):
        kill_all_children(venster)

        name_label = Label(venster, text="Enter Name:")
        name_label.place(relx=0.3, rely=0.4, anchor="center")

        name_entry = Entry(venster)
        name_entry.place(relx=0.5, rely=0.4, anchor="center")

        race_label = Label(venster, text=f"Select Race: {races[CharacterCreationScreen.current_race_index]}")
        race_label.place(relx=0.3, rely=0.5, anchor="center")

        right_arrow_button = Button(venster, text="➡",
                                    command=lambda: CharacterCreationScreen.next_character(race_label))
        right_arrow_button.place(relx=0.6, rely=0.5, anchor="center")

        left_arrow_button = Button(venster, text="⬅",
                                   command=lambda: CharacterCreationScreen.prev_character(race_label))
        left_arrow_button.place(relx=0.4, rely=0.5, anchor="center")

        character_image = Image.open(r"Images/gollum.png")
        character_image = character_image.resize((200, 200), Image.LANCZOS)
        character_image = ImageTk.PhotoImage(character_image)


        character_label = Label(venster, text="Character Preview", image=character_image, compound="bottom")
        character_label.image = character_image
        character_label.place(relx=0.5, rely=0.6, anchor="center")

        original_image2 = Image.open(r"Images/home_button.png")
        original_image2 = original_image2.resize((100, 100), Image.LANCZOS)
        voorbeeld_image2 = ImageTk.PhotoImage(original_image2)

        create_button = Button(venster, text="Create Character", command=lambda: CharacterCreationScreen.create_character(name_entry, race_label))
        create_button.place(relx=0.5, rely=0.8, anchor="center")
        end_button2 = Label(venster, image=voorbeeld_image2, text="Back to character selection", compound="bottom")
        end_button2.image = voorbeeld_image2
        end_button2.bind("<Button-1>", lambda click_event: goto_user_created_characters(venster))
        end_button2.place(relx=0.5, rely=1.0, anchor="center")

    @staticmethod
    def next_character(race_label):
        CharacterCreationScreen.current_race_index = (CharacterCreationScreen.current_race_index + 1) % len(races)
        race_label.config(text=f"Select Race: {races[CharacterCreationScreen.current_race_index]}")

    @staticmethod
    def prev_character(race_label):
        CharacterCreationScreen.current_race_index = (CharacterCreationScreen.current_race_index - 1) % len(races)
        race_label.config(text=f"Select Race: {races[CharacterCreationScreen.current_race_index]}")

    @staticmethod
    def create_character(name_entry, race_label):
        name = name_entry.get()
        selected_race = race_label.cget("text").split(":")[1].strip()

        print("Name:", name)
        print("Race:", selected_race)

        with open("documenten/characters.txt", "a") as file:
            file.write(f"{name},{selected_race}\n")

        # Update the combobox
        CharacterCreationScreen.show_existing_characters(None, CharacterCreationScreen.character_dropdown)

    @staticmethod
    def show_existing_characters(venster, character_dropdown):
        characters_from_file = CharacterCreationScreen.load_characters_from_file("documenten/characters.txt")
        character_dropdown['values'] = [f"{char[0]} - {char[1]}" for char in characters_from_file]
        character_dropdown.set("")  # default selection empty

def goto_character_creation(venster):
    from character_selection import make_character_selection_screen
    make_character_selection_screen(venster)
def goto_user_created_characters(venster):

    make_character_creation_screen(venster)
def make_character_creation_screen(venster):
    kill_all_children(venster)

    original_image = Image.open(r"Images/stickman_echt.png")
    voorbeeld_image = ImageTk.PhotoImage(original_image)

    start_button = Label(venster, text="Create new character", image=voorbeeld_image, compound="bottom")
    start_button.image = voorbeeld_image
    start_button.bind("<Button-1>", lambda click_event: CharacterCreationScreen.create_character_screen(venster))
    start_button.place(relx=0.35, rely=0.2, anchor="center")

    # Combobox
    CharacterCreationScreen.character_dropdown = ttk.Combobox(venster, font=("Arial", 16), state="readonly")
    CharacterCreationScreen.character_dropdown.place(relx=0.65, rely=0.35, anchor="center")
    CharacterCreationScreen.character_dropdown.bind("<Button-1>", lambda click_event: CharacterCreationScreen.show_existing_characters(venster, CharacterCreationScreen.character_dropdown))

    # Start button for adventure selection
    original_image3 = Image.open(r"Images/adventure_button.png")
    original_image3 = original_image3.resize((200, 200), Image.LANCZOS)
    voorbeeld_image3 = ImageTk.PhotoImage(original_image3)

    start_adventure_button = Label(venster, image=voorbeeld_image3, text="Start Adventure", compound="bottom")
    start_adventure_button.image = voorbeeld_image3
    start_adventure_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    start_adventure_button.place(relx=0.35, rely=0.7, anchor="center")


    show_existing_button = Label(venster, text="Show existing characters", image=voorbeeld_image, compound="bottom")
    show_existing_button.image = voorbeeld_image
    show_existing_button.place(relx=0.65, rely=0.2, anchor="center")

    original_image2 = Image.open(r"Images/home_button.png")
    original_image2 = original_image2.resize((200, 200), Image.LANCZOS)
    voorbeeld_image2 = ImageTk.PhotoImage(original_image2)

    end_button2 = Label(venster, image=voorbeeld_image2, text="Back to character selection", compound="bottom")
    end_button2.image = voorbeeld_image2
    end_button2.bind("<Button-1>", lambda click_event: goto_character_creation(venster))
    end_button2.place(relx=0.5, rely=0.7, anchor="center")


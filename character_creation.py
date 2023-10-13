from tkinter import Label, Entry, Button, Tk, ttk, messagebox
from PIL import Image, ImageTk
from character_selection import goto_adventure_selection_screen
from main import kill_all_children

races = ["Hobbit_Male", "Hobbit_Female", "Elf_Male", "Elf_Female", "Dwarf_Male", "Dwarf_Female", "Human_Male", "Human_Female"]
race_images = {
    "Hobbit_Male": "images/hobbit_male.png",
    "Hobbit_Female": "images/hobbit_female.png",
    "Elf_Male": "images/elf_male.png",
    "Elf_Female": "images/elf_female.png",
    "Dwarf_Male": "images/dwarf_male.png",
    "Dwarf_Female": "images/dwarf_female.png",
    "Human_Male": "images/human_male.png",
    "Human_Female": "images/human_female.png"
}

def get_selected_character_image(selected_index):
    characters=[]
    try:
        with open("characters.txt", 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                character = {
                    "name": parts[0],
                    "race": parts[1],
                    "sex": parts[2],
                    "image": parts[3]
                }
                characters.append(character)
    except FileNotFoundError:
        pass

    if 0 <= selected_index < len(characters):
        return characters[selected_index]["image"]
    else:
        return None





def get_selected_character_info(selected_index, characters_file_path):
    characters = []

    try:
        with open(characters_file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                character = {
                    "name": parts[0],
                    "race": parts[1],
                    "sex": parts[2],
                    "image": parts[3]
                }
                characters.append(character)
    except FileNotFoundError:
        pass

    if 0 <= selected_index < len(characters):
        return characters[selected_index]
    else:
        return None




class CharacterCreationScreen:
    current_race_index = 0
    character_dropdown = None
    character_label = None

    @staticmethod
    def start_adventure(venster):
        selected_index = CharacterCreationScreen.character_dropdown.current()
        selected_character_info = get_selected_character_info(selected_index, "documenten/characters.txt")

        if selected_character_info:
            print("Selected Character Info:", selected_character_info)
        else:
            print("No character selected.")

    @staticmethod
    def delete_character(character_dropdown):
        selected_index = character_dropdown.current()
        if selected_index != -1:
            # are you sure
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this character?")

            if confirmation:
                characters_from_file = CharacterCreationScreen.load_characters_from_file("documenten/characters.txt")

                # delete character
                updated_characters = [char for i, char in enumerate(characters_from_file) if i != selected_index]

                # update file
                with open("documenten/characters.txt", "w") as file:
                    for char in updated_characters:
                        file.write(f"{char[0]},{char[1]},{char[2]},{char[3]}\n")

                # update combobox
                CharacterCreationScreen.show_existing_characters(None, character_dropdown, None)

    @staticmethod
    def load_characters_from_file(file_path):
        characters = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    characters.append((parts[0], parts[1], parts[2], parts[3]))
        except FileNotFoundError:
            pass
        return characters

    @staticmethod
    def next_character(race_label):
        CharacterCreationScreen.current_race_index = (CharacterCreationScreen.current_race_index + 1) % len(races)
        race_label.config(text=f"Select Race: {races[CharacterCreationScreen.current_race_index]}")

        # update the photo
        CharacterCreationScreen.update_character_image()

    @staticmethod
    def prev_character(race_label):
        CharacterCreationScreen.current_race_index = (CharacterCreationScreen.current_race_index - 1) % len(races)
        race_label.config(text=f"Select Race: {races[CharacterCreationScreen.current_race_index]}")

        # update the photo
        CharacterCreationScreen.update_character_image()

    @staticmethod
    def update_character_image():
        character_image_path = race_images[races[CharacterCreationScreen.current_race_index]]
        character_image = Image.open(character_image_path)
        character_image = character_image.resize((200, 200), Image.LANCZOS)
        character_image = ImageTk.PhotoImage(character_image)

        CharacterCreationScreen.character_label.config(image=character_image)
        CharacterCreationScreen.character_label.image = character_image

    @staticmethod
    def create_character(name_entry, race_label, root):
        name = name_entry.get()
        selected_race = races[CharacterCreationScreen.current_race_index]  # Use races list directly

        if not name or not selected_race:
            print("Please enter a valid name and select a race.")
            return

        print("Name:", name)
        print("Race:", selected_race)

        with open("documenten/characters.txt", "a") as file:
            file.write(f"{name},{selected_race},male,{race_images[races[CharacterCreationScreen.current_race_index]]}\n")

        # Update the character image
        CharacterCreationScreen.update_character_image()

        # Update the combobox
        CharacterCreationScreen.show_existing_characters(None, CharacterCreationScreen.character_dropdown, None)
        goto_user_created_characters(root)

    @staticmethod
    def show_existing_characters(venster, character_dropdown, start_adventure_button):
        characters_from_file = CharacterCreationScreen.load_characters_from_file("documenten/characters.txt")
        character_dropdown['values'] = [f"{char[0]} - {char[1]}" for char in characters_from_file]
        character_dropdown.set("")  # default selection empty

        start_adventure_button["state"] = "normal" if characters_from_file else "disabled"

    @staticmethod
    def create_character_screen(venster):
        kill_all_children(venster)

        name_label = Label(venster, text="Enter Name:", bg="#603000", fg="white")
        name_label.place(relx=0.3, rely=0.2, anchor="center")

        name_entry = Entry(venster)
        name_entry.place(relx=0.5, rely=0.2, anchor="center")

        race_label = Label(venster, text=f"Select Race: {races[CharacterCreationScreen.current_race_index]}", bg="#603000", fg="white")
        race_label.place(relx=0.3, rely=0.4, anchor="center")

        right_arrow_button = Button(venster, text="➡",
                                    command=lambda: CharacterCreationScreen.next_character(race_label),bg="#603000", fg="white")
        right_arrow_button.place(relx=0.6, rely=0.4, anchor="center")

        left_arrow_button = Button(venster, text="⬅",
                                   command=lambda: CharacterCreationScreen.prev_character(race_label),bg="#603000", fg="white")
        left_arrow_button.place(relx=0.4, rely=0.4, anchor="center")

        character_image_path = race_images[races[CharacterCreationScreen.current_race_index]]
        character_image = Image.open(character_image_path)
        character_image = character_image.resize((230, 230), Image.LANCZOS)
        character_image = ImageTk.PhotoImage(character_image)

        CharacterCreationScreen.character_label = Label(venster, text="Character Preview", image=character_image, compound="bottom", bg="#603000", fg="white")
        CharacterCreationScreen.character_label.image = character_image
        CharacterCreationScreen.character_label.place(relx=0.5, rely=0.4, anchor="center")

        original_image2 = Image.open(r"images/prohibit_sign.png")
        original_image2 = original_image2.resize((35, 35), Image.LANCZOS)
        voorbeeld_image2 = ImageTk.PhotoImage(original_image2)

        create_button = Button(venster, text="Create Character", command=lambda: CharacterCreationScreen.create_character(name_entry, race_label, venster))
        create_button.place(relx=0.5, rely=0.8, anchor="center")

        # Move the button to the top-right corner
        end_button2 = Label(venster, image=voorbeeld_image2, text="Back to\ncharacter selection", compound="bottom", bg="black", fg= "white")
        end_button2.image = voorbeeld_image2
        end_button2.bind("<Button-1>", lambda click_event: goto_user_created_characters(venster))
        end_button2.place(relx=0.95, rely=0.08, anchor="ne")  # Adjusted relx and rely




def goto_character_creation(venster):
    from character_selection import make_character_selection_screen
    make_character_selection_screen(venster)

def goto_user_created_characters(venster):
    make_character_creation_screen(venster)

def make_character_creation_screen(venster):
    kill_all_children(venster)

    original_image = Image.open(r"Images/human_male.png")
    original_image = original_image.resize((200, 200), Image.LANCZOS)
    voorbeeld_image = ImageTk.PhotoImage(original_image)

    start_button = Label(venster, text="Create new character", image=voorbeeld_image, compound="bottom", bg="#603000", fg="white")
    start_button.image = voorbeeld_image
    start_button.bind("<Button-1>", lambda click_event: CharacterCreationScreen.create_character_screen(venster))
    start_button.place(relx=0.35, rely=0.2, anchor="center")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="603000", background="white")

    # Combobox
    CharacterCreationScreen.character_dropdown = ttk.Combobox(venster, font=("Arial", 16), state="readonly")
    CharacterCreationScreen.character_dropdown.place(relx=0.65, rely=0.35, anchor="center")
    CharacterCreationScreen.character_dropdown.bind("<Button-1>", lambda click_event: CharacterCreationScreen.show_existing_characters(venster, CharacterCreationScreen.character_dropdown, start_adventure_button))

    # Start button for adventure selection
    original_image3 = Image.open(r"Images/adventure_button.png")
    original_image3 = original_image3.resize((200, 200), Image.LANCZOS)
    voorbeeld_image3 = ImageTk.PhotoImage(original_image3)

    original_image4 = Image.open(r"Images/human_female.png")
    original_image4 = original_image4.resize((200, 200), Image.LANCZOS)
    voorbeeld_image4 = ImageTk.PhotoImage(original_image4)


    start_adventure_button = Label(venster, image=voorbeeld_image3, text="Start Adventure", compound="bottom",bg="#603000", fg="white")
    start_adventure_button.image = voorbeeld_image3
    start_adventure_button["state"] = "disabled"
    start_adventure_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster, get_selected_character_info(CharacterCreationScreen.character_dropdown.current(),"documenten/characters.txt")))
    start_adventure_button.place(relx=0.5, rely=0.7, anchor="center")  # Centered horizontally

    show_existing_button = Label(venster, text="Show existing characters", image=voorbeeld_image4, compound="bottom",bg="#603000", fg="white")
    show_existing_button.image = voorbeeld_image4
    show_existing_button.place(relx=0.65, rely=0.2, anchor="center")



    original_image2 = Image.open(r"images/prohibit_sign.png")
    original_image2 = original_image2.resize((35, 35), Image.LANCZOS)
    voorbeeld_image2 = ImageTk.PhotoImage(original_image2)

    end_button2 = Label(venster, image=voorbeeld_image2, text="Back to\n character selection", compound="top", bg="black", fg= "white")
    end_button2.image = voorbeeld_image2
    end_button2.bind("<Button-1>", lambda click_event: goto_character_creation(venster))
    end_button2.place(relx=0.92, rely=0.95, anchor="center")

    delete_button_image_proto = Image.open(r"images/bin.png")
    delete_button_image_proto = delete_button_image_proto.resize((50, 50), Image.LANCZOS)
    delete_button_image = ImageTk.PhotoImage(delete_button_image_proto)

    delete_button = Label(venster, text="Delete selected character", image=delete_button_image, compound="bottom", bg="#603000", fg="white")
    delete_button.image = delete_button_image
    delete_button.bind("<Button-1>", lambda click_event: CharacterCreationScreen.delete_character(CharacterCreationScreen.character_dropdown))
    delete_button.place(relx=0.65, rely=0.45, anchor="center")
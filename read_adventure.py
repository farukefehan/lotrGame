def read_adventure(file):
    with open(file, "r", encoding="utf8") as bestand:
        adventure_bestand = bestand.read()
    adventure_bestand_name_screens = adventure_bestand.split("!\n\n")
    data_screens_list = adventure_bestand_name_screens[1:]
    screens_list = []
    for screen in data_screens_list:
        screen_data = screen.split("@\n")
        option_data = screen_data[3].replace("opties;\n", "").split("?\n")
        options_list = []
        for option in option_data:
            data = option.split(":")
            data_list_options = data[1].split(",")
            death_message = "None"
            if data_list_options[1] == "gotoDied" or data_list_options[1] == "gotoWin":
                death_message = data_list_options[3]
            option_dict = {
                "text": data_list_options[0],
                "action": data_list_options[1],
                "admin": data_list_options[2],
                "death_message": death_message

            }
            options_list.append(option_dict)
        question = screen_data[1].replace("question:", "").replace("\"", "")
        image = screen_data[2].replace("image:", "").replace("\"", "")
        screen_dict = {
            "question": question,
            "image": image,
            "options": options_list
        }
        screens_list.append(screen_dict)
    return screens_list

def read_adventure(file):
    with open(file, "r") as bestand:
        adventure_bestand = bestand.read()
    adventure_bestand_name_screens = adventure_bestand.split("!\n\n")
    data_screens_list = adventure_bestand_name_screens[1:]
    screens_list = []
    for screen in data_screens_list:
        screen_data = screen.split(".\n")
        print(screen)
        option_data = screen_data[2].replace("opties;\n", "").split("?\n")
        print(option_data)
        options_list = []
        for option in option_data:
            data = option.split(":")
            data_list_options = data[1].split(",")
            death_message = "None"
            if data_list_options[1] == "gotoDied":
                death_message = data_list_options[3]
            option_dict = {
                "text": data_list_options[0],
                "action": data_list_options[1],
                "admin": data_list_options[2],
                "death_message": death_message

            }
            options_list.append(option_dict)
        print(options_list)
        question = screen_data[1].replace("question:", "").replace("\"", "")
        screen_dict = {
            "question": question,
            "options": options_list
        }
        print(screen_dict)
        screens_list.append(screen_dict)
    print(screens_list)
    return screens_list

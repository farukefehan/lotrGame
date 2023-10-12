def read_adventure(file):
    with open(file, "r", encoding="utf8") as bestand:
        adventure_bestand = bestand.read()
    adventure_bestand_name_screens = adventure_bestand.split("!\n\n")
    data_screens_list = adventure_bestand_name_screens[1:]
    check_point_data = adventure_bestand_name_screens[0]
    checkpoints = check_point_data.split(":")[1]
    print(checkpoints)
    screens_list = []
    screens_list.append(checkpoints)
    print(f"abns: {adventure_bestand_name_screens}")
    for screen in data_screens_list:
        screen_data = screen.split("@\n")
        option_data = screen_data[3].replace("opties;\n", "").split("?\n")
        options_list = []
        for option in option_data:
            data = option.split(":")
            data_list_options = data[1].split(",")
            death_message = "None"
            print(data_list_options)
            if data_list_options[1] == "gotoDied" or data_list_options[1] == "gotoWin":
                death_message = data_list_options[3]
            try:
                if data_list_options[3] == "CP":
                    death_message = data_list_options[3]
            except:
                death_message = "None"
            print(death_message)
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
        print(screens_list[0])
    return screens_list

eits = ["Olamida", "Richard", "Emmanuel Odero", "Ahmed", "Clinton", "Siri"]
eits[3] = "Clinton"

for position in range(len(eits)):
    display_number = position + 1
    eit_name = eits[position]
    print(display_number, " - ", eit_name)
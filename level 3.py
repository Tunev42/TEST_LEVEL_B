while True:
    print("Какая сейчас погода (дождь, солнечная, пасмурная или снег)")
    weather = input()
    if weather == "дождь":
        print("Какая сейчас температура (0 или 10?")
        temp_1 = int(input())
        if temp_1 >= 0:
            print("Вам нужно надеть кофту, штаны и дождевик или зонтик")
            break
        elif temp_1 >= 10:
            print("Нужно надеть ветровку, штаны и дождевик или зонтик")
        else:
            print("Введите градус занова")
            continue
    elif weather == "солнечная":
        print("Какая сейчас температура (10 или 20)?")
        temp_2 = int(input())
        if temp_2 >= 10:
            print("Вам нужно одеть кофту, штаны,")
            break
        elif temp_2 >= 20:
            print("Нужно надеть майку и шорты")
        else:
            print("Введите градус занова")
            continue
    elif weather == "пасмурная":
        print("Какая сейчас температура")
        temp_3 = int(input())
        if temp_3 >= 10:
            print("Нужно надеть ветровку и штаны")
            break
        elif temp_3 >= 20:
            print("Нужно надеть футболку и шорты")
            break
        else:
            print("Введите градус занова")
            continue
    elif weather == "снег":
        print("Введите гардус(-10 или -20)")
        temp_4 = int(input())
        if temp_4 >= -10:
            print("Нужно надеть куртку и подштаники и штаны")
            break
        elif temp_4 >= -20:
            print("Вам нужно надеть кофту, куртку и тёплые штаны")
            break
        else:
            print("Введите снова (-15 или - 30)")
            continue
    else:
        print("Введите погоду занова")
        continue

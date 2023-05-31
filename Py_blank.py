class Man:
    def __init__(man, name, age):
        man.name = name
        man.age = age

    def talk(man):
        s = f"Ten toi la {man.name} toi nam nay {man.age} tuoi."
        print(s)


man1 = Man("Duong", 24)
man2 = Man("Huyen", 30)
man1.talk()
man2.talk()

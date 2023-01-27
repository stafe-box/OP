import actions

while True:
    print(
        "\nВыберите действие:" +
        "\n\t1 - Показать всех преподавателей" +
        "\n\t2 - Показать все дисциплны" +
        "\n\t3 - Показать одного препрдавателя" +
        "\n\t4 - Добавить преподавателя" +
        "\n\t5 - Добавить дисциплину" +
        "\n\t6 - Добавить вид контроля" +
        "\n\t7 - Связать дисциплину и преподавателей" +
        "\n\t8 - Выйти\n")
    choose = int(input(">>> "))
    match choose:
        case 1:
            actions.all_teachers()
        case 2:
            actions.all_disciplines()
        case 3:
            actions.one_teacher()
        case 4:
            actions.add_teacher()
        case 5:
            actions.add_discipline()
        case 6:
            actions.add_kind_control()
        case 7:
            actions.append_teachers_to_disciplines()
        case 8:
            exit(0)
        case _:
            actions.warn("Такого варианта действия нет")


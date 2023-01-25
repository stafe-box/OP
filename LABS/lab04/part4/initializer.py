#initializer

import actions


# Добавление преподавателей
actions.add_teacher("Иванов Иван Иванович")
actions.add_teacher("Гончаров Дмитрий Алексеевич")
actions.add_teacher("Покачеев Сергей Михайлович")
actions.add_teacher("Михайлова Нина Петровна")

# Добавление вида контроля
actions.add_kind_control("Зачет")
actions.add_kind_control("Зачет с оценкой")
actions.add_kind_control("Экзамен")

# Добавление дисциплин
actions.add_discipline(1, "Математика", 5, 2, 1)
actions.add_discipline(2, "Русский язык", 10, 5, 0)
actions.add_discipline(3, "Информатика", 2, 1, 1)
actions.add_discipline(1, "История", 3, 0, 8)

# Назначение преподавателей на дисциплины
actions.append_teachers_to_disciplines(1, [3, 4])
actions.append_teachers_to_disciplines(2, [1])
actions.append_teachers_to_disciplines(3, [2])
actions.append_teachers_to_disciplines(4, [1, 2, 3, 4])
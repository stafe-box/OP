from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import models


engine = create_engine('sqlite:///sqlite3.db')
session = Session(bind=engine)


def add_kind_control():
    kind = input("Введите название вида контроля>>> ")
    kinds = session.query(models.KindControl).filter(models.KindControl.title.is_(kind))
    if kinds.count() > 0:
        warn("Такой вид контроля уже существует")
        return
    new_kind = models.KindControl(title=kind)
    session.add(new_kind)
    session.commit()
    sucsess("Вид контроля успешно добавлен")


def add_teacher():
    full_name = input("Введите ФИО препрдователя>>> ")
    teachers = session.query(models.Teacher).filter(models.Teacher.full_name.is_(full_name))
    if teachers.count() > 0:
        warn("Такой препрдователь уже существует")
        return
    new_teacher = models.Teacher(full_name=full_name)
    session.add(new_teacher)
    session.commit()
    sucsess("Преподователь успешно добавлен")


def add_discipline():
    name = input('Введите название дисиплины>>> ')
    disciplines = session.query(models.Discipline).filter(
        models.Discipline.discipline_name.is_(name))
    if disciplines.count() > 0:
        warn("Такая дисциплина уже существует")
        return
    kinds = session.query(models.KindControl)
    print ("Выберите вид контроля:")
    for kind in kinds:
        print (f"\t{kind.id} - {kind.title}")
    id_kind = int(input(">>> "))
    if (id_kind > kinds.count()) or (id_kind < 1):
        warn(f"Вид контроля с номером {id_kind} не найден")
        return
    kind = kinds.first()
    lectures = int(input("Введите количество лекций>>> "))
    practices = int(input("Введите количество практик>>> "))
    laboratory = int(input("Введите количество лабораторных>>> "))

    new_discipline = models.Discipline(
        discipline_name=name,
        lectures=lectures,
        practices=practices,
        laboratory=laboratory,
        kind_control_id=kind
    )

    kind.disciplines.append(new_discipline)

    session.add(new_discipline)
    session.commit()
    sucsess("Дисциплина успешно добавлена")


def append_teachers_to_disciplines():
    disciplines = session.query(models.Discipline)
    print ("Выберите дисциплину")
    for discipline in disciplines:
        print (f"\t{discipline.id} - {discipline.discipline_name}")
    id_discipline = int(input(">>> "))
    # k = disciplines.count()
    # print (k)
    nDiscipline = session.query(models.Discipline).filter(models.Discipline.id.is_(id_discipline))
    if not(nDiscipline.exists):
        warn(f"Дисциплина с номером{id_discipline} не найдена")
        return
    all_t = session.query(models.Teacher)
    print("Выберите преподователей")
    for teacher in all_t:
        print(f"\t{teacher.id} - {teacher.full_name}")
    Snums = input("Введите номера через запятую\n>>>")
    id_teachers = Snums.split(", ")
    teachers = session.query(models.Teacher).filter(models.Teacher.id.in_(id_teachers))
    if teachers.count() < 1:
        warn(f"Преподователеи с номерами {id_teachers} не найдены")

    disciplines = session.query(models.Discipline).filter(models.Discipline.id == id_discipline)
    discipline = disciplines.first()

    for teacher in teachers.all():
        discipline.teachers.append(teacher)

        session.add(teacher)

    session.add(discipline)
    session.commit()
    sucsess("Преподователи успешно связанны с дисциплинами")


def all_disciplines():
    disciplines = session.query(models.Discipline).all()
    print("Все дисциплины:")
    for discipline in disciplines:
        print(f"\t{discipline.discipline_name}")

        print("\t|__Преподаватели:")
        for teacher in discipline.teachers:
            print(f"\t|\t|__{teacher.full_name}")

        kind = session.query(models.KindControl).filter(models.KindControl.id == discipline.kind_control_id)
        print(f"\t|__Вид контроля: \n\t\t|__{kind.first().title}\n")
    input("\033[94mНажмите ВВОД чтобы продолжить\033[0m")


def all_teachers():
    teachers = session.query(models.Teacher).all()

    print("Все преподаватели:")
    for teacher in teachers:
        print(f"\tФИО: {teacher.full_name}, число дисциплин: {len(teacher.disciplines)}")
    input("\033[94mНажмите ВВОД чтобы продолжить\033[0m")


def one_teacher():
    name = input("Введите ФИО преподователя >>> ")
    teachers = session.query(models.Teacher).filter(
        models.Teacher.full_name == name)
    if teachers.count() < 1:
        warn("Такого преподователя не сушествует")
        return
    teacher = teachers.first()
    inf = (f"ФИО: {teacher.full_name}, дициплины: ")
    for discipline in teacher.disciplines:
        inf += f"\n\t{discipline.discipline_name}"
    print(inf)
    input("\033[94mНажмите ВВОД чтобы продолжить\033[0m")


def warn(text):
    print(f"\033[93m{text}\033[0m")

def sucsess(text):
    print(f"\033[92m{text}\033[0m")

def fatal(text):
    print(f"\033[91m{text}\033[0m")

from src.lab9.group import Group
from src.lab8.models import Student


def main():
    path = "data/lab09/students.csv"
    group = Group(path)

    print(" ПЕРВОНАЧАЛЬНЫЙ СПИСОК")
    for s in group.list():
        print("  ", s)

    print("ДОБАВЛЕНИЕ СТУДЕНТА")
    new_student = Student(
        fio="Тестовый Студент",
        birthdate="2007-04-25",
        group="БИВТ-25-1",
        gpa=4.4
    )
    group.add(new_student)
    print("Добавлен:", new_student)

    print("ПРОВЕРКА СПИСКА ПОСЛЕ ДОБАВЛЕНИЯ ")
    for s in group.list():
        print("  ", s)

    print("ПОИСК ПО ПОДСТРОКЕ 'Тест'")
    found = group.find("Тест")
    for s in found:
        print("  найден:", s)

    print(" ОБНОВЛЕНИЕ GPA")
    group.update("Тестовый Студент", gpa=4.8)
    print("GPA обновлён.")

    print(" СПИСОК ПОСЛЕ ОБНОВЛЕНИЯ")
    for s in group.list():
        print("  ", s)

    print("УДАЛЕНИЕ")
    group.remove("Тестовый Студент")
    print("Удалён Тестовый Студент")

    print("ФИНАЛЬНЫЙ СПИСОК")
    for s in group.list():
        print("  ", s)


if __name__ == "__main__":
    main()
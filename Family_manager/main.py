from data import tasks_db
from reports_module import (
    report_tasks_n_days,
    report_failed_by_assignee,
    report_in_progress_tasks, 
)





def display_menu():
    print("СЕМЕЙНЫЙ МЕНЕДЖЕР - МЕНЮ ОТЧЕТОВ\n")
    print("1. Посмотреть Отчет 1 (Список всех задач, отсортированный по дате по убыванию, выданных за прошедшие 7 дней)")
    print("2. Посмотреть Отчет 2 (Список всех задач заданного члена семьи, имеющих статус «провалено»)")
    print("3. Посмотреть Отчет 3 (Список всех задач, которые находятся на исполнении (имеют статус «получена» или «в процессе»))")
    print("4. Выйти из программы")
    print()


def display_tasks_localized(tasks_list):

    separator = "-" * 60

    # Словарь для перевода ключей на русский язык, учитывая возможные пробелы/опечатки
    translation_map = {
        "received_datetime": "Получено",
        "received datetime": "Получено",
        "due_datetime": "Срок выполнения",
        "due datetime": "Срок выполнения",
        "assignee": "Исполнитель",
        "description": "Описание",
        "status": "Статус"
    }

    print("\n" + separator)
    print("Список задач:")
    
    for i, task in enumerate(tasks_list):
        print(separator)
        
        # Выводим каждую задачу построчно
        for key, value in task.items():
            # Получаем перевод ключа или используем сам ключ, если перевода нет
            russian_key = translation_map.get(key, key.replace('_', ' ').capitalize())
            # Форматируем вывод с отступами
            print(f"    {russian_key:<20}: {value}")

    print(separator)
    return 'Конец списка'

    

def main():
    def handle_choice(choice):
        match choice:
            case '1':
                print("\n>>> Выбран Отчет 1: Список задач, выданных за прошедшие 7 дней")
                one = report_tasks_n_days(tasks_db, 7)
                print(display_tasks_localized(one))
                return True
            case '2':
                print("\n>>> Выбран Отчет 2: Список задач заданного члена семьи, статус «провалено»\n")
                two = report_failed_by_assignee(tasks_db, 'Сын')
                print(display_tasks_localized(two))
                return True
            case '3':
                print("\n>>> Выбран Отчет 3:Список всех задач, которые находятся на исполнении \n")
                three = report_in_progress_tasks(tasks_db)
                print(display_tasks_localized(three))
                return True
            case '4':
                print("\n>>> Выход из программы. До свидания!")
                return False 
            case _:
                print(f"\n[ОШИБКА] Неверный ввод: '{choice}'. Пожалуйста, введите номер от 1 до 4.")
                return True
        

    should_continue = True
    while should_continue:
        display_menu()
        user_input = input("Введите номер пункта меню (1-4) или '4' для выхода: ").strip()
        should_continue = handle_choice(user_input)
        if should_continue:
            print("\n")

if __name__ == "__main__":
    main()
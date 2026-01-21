from datetime import datetime, timedelta
from sort_module import shell_sort
from data import tasks_db

def parse_datetime(dt_str):
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

def report_tasks_n_days(tasks_db, days_ago_n):
    today = datetime.strptime("2024-05-21", "%Y-%m-%d").date()
    cutoff_date = today - timedelta(days=days_ago_n)

    # Фильтрация задач по дате
    filtered_tasks = [
        task for task in tasks_db
        if parse_datetime(task["received_datetime"]).date() >= cutoff_date
    ]

    # Порядок статусов
    status_order = {
        "не выполнена": 0,  # если появится
        "в процессе": 1,
        "получена": 2,
        "провалена": 3,
        "успешно выполнена": 4
    }

    def sort_key(task):
        date_key = -parse_datetime(task["received_datetime"]).timestamp()
        status_key = status_order.get(task.get("status", ""), 99)
        return (date_key, status_key)

    return shell_sort(filtered_tasks, key=sort_key)



def display_tasks(tasks):
    for task in tasks:
        print(f"{task['received_datetime']} | {task['assignee']} | {task['status']} | {task['description']}")

def main():
    print(">>> Отчет 1: Задачи за последние N дней")

    result = report_tasks_n_days(tasks_db, 7)
    display_tasks(result)

if __name__ == "__main__":
    main()

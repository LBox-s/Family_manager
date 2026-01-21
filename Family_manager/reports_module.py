from datetime import datetime, timedelta
from sort_module import shell_sort
# Функции для генерации отчетов
# Вспомогательная функция для преобразования строк в объекты datetime
from datetime import datetime, timedelta
from sort_module import shell_sort

def parse_datetime(dt_str):
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

def report_tasks_n_days(tasks_db, days_ago_n):
    today = datetime.strptime("2024-05-21", "%Y-%m-%d").date()
    cutoff_date = today - timedelta(days=days_ago_n)

    # Фильтрация задач по дате — ПРИВОДИМ к .date()
    filtered_tasks = [
        task for task in tasks_db
        if parse_datetime(task["received_datetime"]).date() >= cutoff_date
    ]

    # Порядок статусов
    status_order = {
        "не выполнена": 0,
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

# 2. Отчет по проваленным задачам члена семьи(например сына)
def report_failed_by_assignee(tasks_db, assignee_name):
    # Фильтрация: заданный исполнитель и статус "провалена"
    filtered_tasks = [
        task for task in tasks_db
        if task["assignee"] == assignee_name and task["status"] == "провалена"
    ]

    # Ключ сортировки 2: Дата выполнения (убывание) + Краткое описание (возрастание)
    def sort_key_2(task):
        # Дата выполнения убывание
        date_key = -parse_datetime(task["due_datetime"]).timestamp()
        # Описание возрастание (строки сортируются лексикографически по умолчанию)
        description_key = task["description"]
        return (date_key, description_key)
    # Применяем сортировку Шелла
    sorted_tasks = shell_sort(filtered_tasks, key=sort_key_2, reverse=False)
    return sorted_tasks


# 3. Отчет по задачам на исполнении
def report_in_progress_tasks(tasks_db):
    # Фильтрация: статус "получена" или "в процессе"
    filtered_tasks = [
        task for task in tasks_db
        if task["status"] in ["получена", "в процессе"]
    ]

    # Ключ сортировки 3: Имя исполнителя (возрастание), Дата предполагаемого исполнения (возрастание)
    def sort_key_3(task):
        assignee_key = task["assignee"]
        due_date_key = parse_datetime(task["due_datetime"]).timestamp()
        return (assignee_key, due_date_key)

    # Применяем сортировку Шелла
    sorted_tasks = shell_sort(filtered_tasks, key=sort_key_3, reverse=False)
    return sorted_tasks
# база данных
tasks_db = [
    # Задачи для отчета 1 (прошедшие N дней, сортировка по дате (убыв), затем по статусу)
    {
        "received_datetime": "2024-05-21 09:00",
        "due_datetime": "2024-05-21 12:00",
        "assignee": "Мама",
        "description": "Купить продукты по списку (срочно)",
        "status": "провалена"
    },
    {
        "received_datetime": "2024-05-21 10:00",
        "due_datetime": "2024-05-21 14:00",
        "assignee": "Папа",
        "description": "Починить кран на кухне",
        "status": "успешно выполнена"
    },
    {
        "received_datetime": "2024-05-21 11:00",
        "due_datetime": "2024-05-22 10:00",
        "assignee": "Сын",
        "description": "Вынести мусор",
        "status": "в процессе"
    },
    {
        "received_datetime": "2024-05-21 12:00",
        "due_datetime": "2024-05-21 19:00",
        "assignee": "Дочь",
        "description": "Помыть посуду после обеда",
        "status": "получена"
    },
    {
        "received_datetime": "2024-05-20 15:00",
        "due_datetime": "2024-05-20 18:00",
        "assignee": "Мама",
        "description": "Забрать одежду из химчистки",
        "status": "успешно выполнена"
    },
    {
        "received_datetime": "2024-05-20 16:00",
        "due_datetime": "2024-05-20 20:00",
        "assignee": "Папа",
        "description": "Проверить уроки у детей",
        "status": "провалена"
    },

    # Задачи для отчета 2 (заданный член семьи, статус "провалено", сортировка по дате выполнения (убыв) + описание (возр))
    {
        "received_datetime": "2024-05-10 09:00",
        "due_datetime": "2024-05-15 10:00",
        "assignee": "Сын",
        "description": "Заправить свою кровать",
        "status": "провалена"
    },
    {
        "received_datetime": "2024-05-12 10:00",
        "due_datetime": "2024-05-14 18:00",
        "assignee": "Сын",
        "description": "Сделать домашнее задание",
        "status": "провалена"
    },
     {
        "received_datetime": "2024-05-13 10:00",
        "due_datetime": "2024-05-14 18:00", # Та же дата, что и выше, для проверки вторичной сортировки по описанию
        "assignee": "Сын",
        "description": "Погулять с собакой",
        "status": "провалена"
    },
    {
        "received_datetime": "2024-05-01 09:00",
        "due_datetime": "2024-05-01 10:00",
        "assignee": "Сын",
        "description": "Почистить зубы",
        "status": "провалена"
    },

    # Задачи для отчета 3 (статус "получена" или "в процессе", сортировка по имени (возр), дата выполнения (возр))
    {
        "received_datetime": "2024-05-22 09:00",
        "due_datetime": "2024-05-22 11:00",
        "assignee": "Дочь",
        "description": "Разобрать игрушки",
        "status": "получена"
    },
    {
        "received_datetime": "2024-05-22 08:00",
        "due_datetime": "2024-05-22 10:00", # Более ранняя дата выполнения, чем у предыдущей
        "assignee": "Дочь",
        "description": "Собрать портфель",
        "status": "в процессе"
    },
    {
        "received_datetime": "2024-05-22 10:00",
        "due_datetime": "2024-05-23 09:00",
        "assignee": "Мама",
        "description": "Приготовить ужин",
        "status": "в процессе"
    },
    {
        "received_datetime": "2024-05-22 11:00",
        "due_datetime": "2024-05-22 18:00",
        "assignee": "Папа",
        "description": "Полить цветы на балконе",
        "status": "получена"
    },
    {
        "received_datetime": "2024-05-22 12:00",
        "due_datetime": "2024-05-22 19:00",
        "assignee": "Папа",
        "description": "Оплатить счета за интернет",
        "status": "в процессе"
    },

    # Дополнительные задачи для достижения общего количества в 25 записей
    {
        "received_datetime": "2024-05-18 10:00",
        "due_datetime": "2024-05-18 12:00",
        "assignee": "Мама",
        "description": "Погладить белье",
        "status": "успешно выполнена"
    },
    {
        "received_datetime": "2024-05-17 10:00",
        "due_datetime": "2024-05-17 14:00",
        "assignee": "Папа",
        "description": "Поменять лампочку в коридоре",
        "status": "успешно выполнена"
    },
    {
        "received_datetime": "2024-05-16 10:00",
        "due_datetime": "2024-05-16 11:00",
        "assignee": "Сын",
        "description": "Убрать в своей комнате",
        "status": "успешно выполнена"
    },
    {
        "received_datetime": "2024-05-15 10:00",
        "due_datetime": "2024-05-15 12:00",
        "assignee": "Дочь",
        "description": "Вытереть пыль",
        "status": "успешно выполнена"
    },
     {
        "received_datetime": "2024-05-14 10:00",
        "due_datetime": "2024-05-14 16:00",
        "assignee": "Мама",
        "description": "Записаться к врачу",
        "status": "успешно выполнена"
    },
    {
        "received_datetime": "2024-05-13 10:00",
        "due_datetime": "2024-05-13 18:00",
        "assignee": "Папа",
        "description": "Помыть машину",
        "status": "провалена"
    },
    {
        "received_datetime": "2024-05-12 10:00",
        "due_datetime": "2024-05-12 11:00",
        "assignee": "Сын",
        "description": "Покормить кота",
        "status": "успешно выполнена"
    },
     {
        "received_datetime": "2024-05-11 10:00",
        "due_datetime": "2024-05-11 13:00",
        "assignee": "Дочь",
        "description": "Позвонить бабушке",
        "status": "успешно выполнена"
    },
    {
        "received_datetime": "2024-05-10 10:00",
        "due_datetime": "2024-05-10 15:00",
        "assignee": "Мама",
        "description": "Испечь пирог к приходу гостей",
        "status": "успешно выполнена"
    },
    {
        "received_datetime": "2024-05-09 10:00",
        "due_datetime": "2024-05-09 18:00",
        "assignee": "Папа",
        "description": "Заменить фильтр для воды",
        "status": "успешно выполнена"
    }
]
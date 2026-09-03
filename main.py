import json
import datetime
def add_task(tasks):

    while True:
        task_title = input("Введите название: ").strip()
        if task_title:
            break
        print("\nОшибка: название задачи не может быть пустым!\n")

    while True:
        task_description = input("Введите описание: ").strip()
        if task_description:
            break
        print("\nОшибка: описание задачи не может быть пустым!\n")


    while True:
        task_priority = input("Выберите приоритет задачи:"
                              "\n1. High"
                              "\n2. Medium"
                              "\n3. Low"
                              "\nПриоритет: ")

        if task_priority == "1":
            task_priority = "High"
            break
        elif task_priority == "2":
            task_priority = "Medium"
            break
        elif task_priority == "3":
            task_priority = "Low"
            break
        else:
            print("\nОшибка: такого приоритета не существует. Введите 1, 2 или 3.\n")


    while True:
        task_deadline = input("Введите дедлайн в формате ГГГГ-ММ-ДД или нажмите Enter: ").strip()
        if not task_deadline:
            deadline_date = "Нет"
            break

        try:
            valid_date = datetime.datetime.strptime(task_deadline, "%Y-%m-%d")
            deadline_date = valid_date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("\nОшибка! Неверный формат или несуществующая дата. Попробуйте снова (ГГГГ-ММ-ДД).\n")


    new_id = max((task.get("id", 0) for task in tasks), default=0) + 1
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    task = {
        "id": new_id,
        "title": task_title,
        "description": task_description,
        "completed": False,
        "priority": task_priority,
        "created_at": create_time,
        "deadline": deadline_date
    }
    tasks.append(task)
    save_tasks(tasks)
    print("\nВы успешно записали задачу!\n")


def show_tasks(tasks):
    if not tasks:
        print("\nСписок задач пуст.\n")
        return
    else:
        print("====Список задач====")

        for task in tasks:
            status = "[x]" if task.get("completed", False) else "[]"
            task_id = task.get("id")
            task_title = task.get("title")
            task_description = task.get("description")
            task_priority = task.get("priority")
            task_created_at = task.get("created_at")
            task_deadline = task.get("deadline")

            print(f"\n{status} ID: {task_id} "
                  f"\nНазвание: {task_title} "
                  f"\nОписание: {task_description}"
                  f"\nПриоритет: {task_priority}"
                  f"\nВремя создания: {task_created_at}"
                  f"\nДедлайн: {task_deadline}\n")


def complete_task(tasks):
    id_number = input("Введите номер задачи, которую вы выполнили: ")

    if id_number.isdigit():
        id_target = int(id_number)
        for task in tasks:
            if task.get('id') == id_target:
                task["completed"] = True
                print(f"\nЗадача {id_target} выполнена!\n")
                break
        else:
            print(f"\nЗадачи {id_number} не существует!\n")

        save_tasks(tasks)
    else:
        print ("\nID должен быть числом.\n")
    return


def delete_task(tasks):
    id_number = input("Введите номер задачи, которую вы хотите удалить: ")

    if id_number.isdigit():
        id_target = int(id_number)
        for task in tasks:
            if task.get('id') == id_target:
                tasks.remove(task)
                print(f"\nЗадача {id_target} удалена!\n")
                break
        else:
            print(f"\nЗадачи {id_number} не существует!\n")

        save_tasks(tasks)
    else:
        print("\nНекорректный ввод. Введите конкретное число!\n")
    return

def show_statistics(tasks):
    task_count = len(tasks)
    completed_tasks = 0
    uncompleted_tasks = 0
    if not tasks:
        print("\nСписок задач пока пуст, статистика отсутствует!\n")
        return

    for task in tasks:
        if task.get("completed", False):
            completed_tasks += 1
        else:
            uncompleted_tasks += 1

    complete_percent = int(completed_tasks / task_count * 100)

    print(
          f"\n====Статистика====\n"
          f"\nВсего задач: {task_count}\n"
          f"Выполнено: {completed_tasks}\n"
          f"Не выполнено: {uncompleted_tasks}\n"
          f"Процент выполнения: {complete_percent}%\n"
          )
    return


def search_task(tasks):
    task_word = input("Поиск: ").strip().lower()
    if not task_word:
        print("\nПоисковый запрос не может быть пустым!\n")
        return

    found = False

    for task in tasks:
        if task_word in task.get("title", " ").lower():
            task_title = task.get("title")
            task_id = task.get("id")
            print(f"ID: {task_id} -", task_title)
            found = True

    if not found:
        print("\nТаких задач не найдено!\n")

    return


def priority_filter(tasks):
    while True:
        task_priority = input("Выберите приоритет задачи:"
                              "\n1. High"
                              "\n2. Medium"
                              "\n3. Low"
                              "\nПриоритет: ")
        if task_priority.isdigit() and 1<= int(task_priority) <= 3:
            if task_priority == "1":
                task_priority = "high"
            elif task_priority == "2":
                task_priority = "medium"
            elif task_priority == "3":
                task_priority = "low"

            break

        else:
            print ("\nОшибка, введите число от 1 до 3\n")

    filtered_tasks = []
    for task in tasks:
        if task_priority == task.get("priority", " ").lower():
            filtered_tasks.append(task)

    if filtered_tasks:
        print(f"\nСписок задач с приоритетом {task_priority}: \n")
        show_tasks(filtered_tasks)
    else:
        print("\nТаких задач не найдено.\n")


def overdue_tasks(tasks):
    overdue_tasks_list = []
    if not tasks:
        print("\nСписок задач пока пуст.\n")
        return

    for task in tasks:
        deadline_str = task.get("deadline", False)
        if not deadline_str or deadline_str == "Нет":
            continue
        deadline_time = datetime.datetime.strptime(task.get("deadline"), "%Y-%m-%d").date()
        current_time = datetime.date.today()
        if deadline_time < current_time and not task.get("completed", False):
            overdue_tasks_list.append(task)

    if overdue_tasks_list:
        print(f"\nСписок просроченных задач: \n")
        show_tasks(overdue_tasks_list)
    else:
        print("\nПросроченные задачи отсутствуют.\n")


def sorted_tasks(tasks):

    sorted_tasks_list = []

    if not tasks:
        print("\nСписок задач пока пуст, статистика отсутствует!\n")
        return

    while True:
        task_priority = input("Выберите сортировку:"
                              "\n1. По ID"
                              "\n2. По названию"
                              "\n3. По статусу"
                              "\n4. По дате создания"
                              "\nВыбор: ")


        if task_priority == "1":
            sorted_tasks_list = sorted(tasks, key=lambda task: task.get("id", 0))
            break

        elif task_priority == "2":
            sorted_tasks_list = sorted(tasks, key=lambda task: task.get("title", " ").lower())
            break

        elif task_priority == "3":
            sorted_tasks_list = sorted(tasks, key=lambda task: task.get("completed", False))
            break

        elif task_priority == "4":
            sorted_tasks_list = sorted(tasks, key=lambda task: task.get("created_at", " "))
            break

        else:
            print("\nОшибка: такой сортировки не существует. Введите 1, 2, 3 или 4.\n")

    print("\nСписок успешно отсортирован!\n")

    show_tasks(sorted_tasks_list)

    tasks.clear()
    tasks.extend(sorted_tasks_list)
    save_tasks(tasks)


def save_tasks(task):
    with open('tasks.json', 'w', encoding='utf-8') as task_file:
        json.dump(task, task_file, ensure_ascii=False, indent=4)
    return


def main():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as task_file:
            tasks = json.load(task_file)
    except FileNotFoundError:
        tasks = []
    except json.decoder.JSONDecodeError:
        print("\nОшибка: Файл с задачами (tasks.json) поврежден!")
        print("Загрузка отменена во избежание потери данных. Исправьте структуру JSON-файла.\n")
        return
    while True:
        print("=== Task Manager ==="
                  "\n1. Показать задачи"
                  "\n2. Добавить задачу"
                  "\n3. Завершить задачу"
                  "\n4. Удалить задачу"
                  "\n5. Найти задачи"
                  "\n6. Показать статистику"
                  "\n7. Показать задачи по приоритету"
                  "\n8. Показать просроченные задачи"
                  "\n9. Сортировка задач"
                  "\n0. Выход")

        choice = input ("Выберите пункт: ")
        if choice.isdigit() and 0 <= int(choice) <=9:

            if choice == "0":
                break
            elif choice == "1":
                show_tasks(tasks)
            elif choice == "2":
                add_task(tasks)
            elif choice == "3":
                complete_task(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                search_task(tasks)
            elif choice == "6":
                show_statistics(tasks)
            elif choice == "7":
                priority_filter(tasks)
            elif choice == "8":
                overdue_tasks(tasks)
            elif choice == "9":
                sorted_tasks(tasks)

        else:
            print("\nОшибка: введите число от 0 до 9.\n")



if __name__ == '__main__':
    main()



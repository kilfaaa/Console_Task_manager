import json
import datetime
def add_task(tasks):

    task_title = input("Введите название: ")
    task_description = input ("Введите описание: ")
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

    new_id = max((task.get("id", 0) for task in tasks), default=0) + 1
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    task = {
        "id": new_id,
        "title": task_title,
        "description": task_description,
        "completed": False,
        "priority": task_priority,
        "created_at": create_time
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

            print(f"\n{status} ID: {task_id} \nНазвание: {task_title} \nОписание: {task_description}\nПриоритет: {task_priority}\n")


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
    task_priority = input("Введите приоритет для фильтрации задач \n(high, medium, low): ").strip().lower()
    if not task_priority:
        print("\nОшибка: ввод пустой!\n")
        return

    filtered_tasks = []
    for task in tasks:
        if task_priority in task.get("priority", " ").lower():
            filtered_tasks.append(task)

    if filtered_tasks:
        print(f"\nСписок задач с приоритетом {task_priority}: \n")
        show_tasks(filtered_tasks)
    else:
        print ("\nТаких задач не найдено.\n")


    return


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
        tasks = []

    while True:
        print("=== Task Manager ==="
                  "\n1. Показать задачи"
                  "\n2. Добавить задачу"
                  "\n3. Завершить задачу"
                  "\n4. Удалить задачу"
                  "\n5. Найти задачи"
                  "\n6. Показать статистику"
                  "\n7. Показать задачи по приоритету"
                  "\n0. Выход")

        choice = input ("Выберите пункт: ")
        if choice.isdigit():

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
        else:
            print("\nВведите корректное число.\n")



if __name__ == '__main__':
    main()



import json

def add_task(tasks):

    task_title = input("Введите название: ")
    task_description = input ("Введите описание: ")

    new_id = max((task.get("id", 0) for task in tasks), default=0) + 1
    task = {
        "id": new_id,
        "title": task_title,
        "description": task_description,
        "completed": False
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

            print(f"\n{status} ID: {task_id} \nНазвание: {task_title} \nОписание: {task_description}\n")

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
        else:
            print("\nВведите корректное число.\n")



if __name__ == '__main__':
    main()



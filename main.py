import json


def main():

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



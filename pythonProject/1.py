from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "+" if self.completed else "✗"
        return f"{status} {self.title} (Дедлайн: {self.deadline.strftime('%Y-%m-%d')})    Опис: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        task = Task(title, description, deadline)
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return True
        return False

    def list_tasks(self):
        if not self.tasks:
            return "Завдань поки що немає."
        return "".join([str(task) for task in self.tasks])

if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("Меню:")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Відмітити завдання як виконане")
        print("4. Переглянути список завдань")
        print("5. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            title = input("Введіть назву завдання: ")
            description = input("Введіть опис завдання: ")
            deadline = input("Введіть дедлайн (YYYY-MM-DD): ")
            manager.add_task(title, description, deadline)
            print("Завдання додано!")

        elif choice == "2":
            title = input("Введіть назву завдання для видалення: ")
            manager.remove_task(title)
            print("Завдання видалено!")

        elif choice == "3":
            title = input("Введіть назву завдання, яке виконано: ")
            if manager.mark_task_completed(title):
                print("Завдання відмічено як виконане!")
            else:
                print("Завдання не знайдено!")

        elif choice == "4":
            print("Список завдань:")
            print(manager.list_tasks())

        elif choice == "5":
            print("До побачення!")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")

from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        tasks_to_clean = []
        for task in self.tasks:
            if task.completed:
                tasks_to_clean.append(task)
        for task in tasks_to_clean:
            self.tasks.remove(task)
        return f"Cleared {len(tasks_to_clean)} tasks."

    def view_section(self):
        result = ''
        result += "Section " + self.name + ':' + '\n'
        for task in self.tasks:
            result += task.details() + '\n'
        return result


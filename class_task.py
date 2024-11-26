class Task:
    def __init__(self, name, priority, due_date, points):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.points = points
        

    def compiler(self):
        task_list = []
        task_list.append(self.task_name)
        task_list.append(self.points)

        for task in task_list:
            return task
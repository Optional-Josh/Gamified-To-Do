class Task:
    def __init__(self, name, priority, due_date, points, status):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.points = points
        self.status = status

    def compiler(self):
        task_list = []
        dict = {
            'name':self.name,
            'priority':self.priority,
            'points':self.points,
            'due date':self.due_date,
            'status':self.status
        }
        task_list.append(dict)

        for task in task_list:
            for key, value in task.items():
                task_list.append((key, value))

        return task_list
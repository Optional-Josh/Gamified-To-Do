class Task:
    def __init__(self, task_name, points):
        self.task_name = task_name
        self.points = points

    def compiler(self):
        task_list = []
        task_list.append(self.task_name)
        task_list.append(self.points)

        for task in task_list:
            return task
class Task:
    def __init__(self, profile, priority, due_date, points, status):
        self.task = {
            'name':profile,
            'priority':priority,
            'points':points,
            'due date':due_date,
            'status':status
        }



    def compiler(self):
        tasks_list = []
        compiled = self.task
        tasks_list.append(compiled)

        for task in tasks_list:
            for key, value in task.items():
                print(key, value)
class Task:
    def __init__(self, profile, description, due_date, points, status):
        # class attributes
        # referend to class profile
        self.profile = profile
        self.description = description
        self.due_date = due_date
        self.points = points
        self.status = status

        self.task = {
            'name':self.profile,
            'description':self.description,
            'points':self.points,
            'due date':self.due_date,
            'status':self.status
        }
    
    def test(self):
        status = self.status
        if status:
            self.profile.xp += self.points
            self.profile.advance_level()

        


    def compiler(self):
        tasks_list = []
        compiled = self.task
        tasks_list.append(compiled)

        for task in tasks_list:
            for key, value in task.items():
                print(key, value)
class Profile:
    def __init__(self, name, xp, level):
        self.name = name
        self.level = level
        self.xp = xp
        self.to_level_next = level * 25

        self.task = []

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, XP: {self.xp}, Next Level: {self.to_level_next}"
    
    def add_task(self, description, due_date, points, status):
        compiled_task_details = {
            'name':self.name,
            'description':description,
            'points':points,
            'due date':due_date,
            'status':status
        }
        self.task.append(compiled_task_details)

    # checks if task status is complete and adds points to xp in class profile
    def check_status(self):
        for detail in self.task:
                if detail['status']:
                    self.xp += detail['points']

    # check is xp is equal to level next requirement
    def advance_level(self):
        while self.xp >= self.to_level_next:
            self.level += 1
            self.xp = 0 
            self.to_level_next * 1.5

            print(f"{self.name} has now reached Level {self.level}!")
            print(f"Your XP has been reset to {self.xp}")
            print(f"To reach the next level you need {self.to_level_next}")
        # level_next = round(self.to_level_next * 1.5)
        # return f"Name: {self.name}\n Level: {self.level}\n XP: {self.xp} \n To Level up {level_next}"


        
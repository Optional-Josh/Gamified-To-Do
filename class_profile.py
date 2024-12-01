
# class profile has name, xp, and level as parameters
# empty list is instantiated for add task method
class Profile:
    def __init__(self, name, xp, level):
        self.name = name
        self.level = level
        self.xp = xp
        self.to_level_next = level * 25

        self.task = []

    # string method that prints when calling out created object
    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, XP: {self.xp}, Next Level: {self.to_level_next}"
    
    # method that compiles input for a task into a dictionary and appended to list in class attribute
    # method requires description, due date, points, and status as parameters
    def add_task(self, description, due_date, points, status):
        compiled_task_details = {
            'name':self.name,
            'description':description,
            'points':points,
            'due date':due_date,
            'status':status
        }
        self.task.append(compiled_task_details)

    # function that checks any tasks in dictionary has a status of true and adds its points to xp of profile
    def check_status(self):
        for detail in self.task:
                if detail['status']:
                    self.xp += detail['points']

    # function that will add a level and distribute points to xp as well as requirement to next level xp
    # note it also carries over excess xp to each level up
    def advance_level(self):
        self.check_status()
        while self.xp >= self.to_level_next:
            self.level += 1
            self.xp = self.xp - self.to_level_next
            self.to_level_next = int(self.to_level_next * 1.5)

            print(f"{self.name} has now reached Level {self.level}!")
            print(f"Your XP has been reset to {self.xp}")
            print(f"To reach the next level you need {self.to_level_next}")
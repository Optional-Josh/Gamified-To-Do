import sys

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
                
                

    def progress_bar(self, current, total, bar_length=40):
        progress = min(current/total, 1)
        block = int(bar_length * progress)
        bar = "#" * block + "-" * (bar_length - block)

        current_display = f"{current/1000:.1f}k" if current >= 1000 else str(current)
        total_display = f"{total/1000:.1f}k" if total >= 1000 else str(total)

        sys.stdout.write(f"Level {self.level} |{bar}| {current_display}/{total_display} XP")
        sys.stdout.flush()

    # function that will add a level and distribute points to xp as well as requirement to next level xp
    # note it also carries over excess xp to each level up
    def advance_level(self):
        self.check_status()
        while self.xp >= self.to_level_next:
            self.level += 1
            self.xp = self.xp - self.to_level_next
            self.to_level_next = int(self.to_level_next * 1.5)

            self.progress_bar(self.xp, self.to_level_next)
            
            print(f"\n🎉 Congratulations! You've reached Level {self.level}!")
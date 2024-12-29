import sys
from datetime import date

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

    def add_category(self):
        categories = ['Household', 'Work', 'Personal', 'Relationship']
        print('1 - Household, 2 - Work, 3 - Personal, 4 - Relationship')
        category_input = input("Category for this task: ")
        if category_input.lower() == '1':
            return categories[0]
        elif category_input.lower() == '2':
            return categories[1]
        elif category_input.lower() == '3':
            return categories[2]
        elif category_input.lower() == '4':
            return categories[3]

    def add_description(self):
        description = input("Description for task: ")
        if description.strip() != "":
            return description
        
    def add_date(self, date_input):
        # date_input = input("Date for this task 'dd/mm/yyyy': ")
        if date_input == "":
            date_input = date.today().strftime("%Y/%m/%d")
        return date_input
    
    def add_diff(self):
        print('1 - Easy, 2 - Medium, 3 - Hard')
        diff_input = input('Difficulty Level for this task: ')
        if diff_input == '0' or diff_input == "":
            diff_level = 1
            return diff_level
        else: 
            converted = int(diff_input)
            return converted

    def add_status(self):
        status = input("Status of Task: ")
        if status.lower() == "completed":
            return status
        else:
            status = "pending"
            return status

    def add_task(self, out_date_input):
        category_input = self.add_category()
        desc_input = self.add_description()
        date_input = self.add_date(out_date_input)
        diff_input = self.add_diff()

        if diff_input == 1:
            pts_input = 5
        elif diff_input == 2:
            pts_input = 10
        elif diff_input == 3:
            pts_input = 15
        stats_input = self.add_status()
        compiled_task_details = {
            'category': category_input,
            'description':desc_input,
            'date':date_input,
            'difficulty': diff_input,
            'points': pts_input,
            'status':stats_input
        }
        self.task.append(compiled_task_details)

    # function that checks any tasks in dictionary has a status of true and adds its points to xp of profile
    def check_status(self, data):
        for detail in data:
                if detail['status'] == 'completed':
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
    def advance_level(self, data):
        self.check_status(data)
        while self.xp >= self.to_level_next:
            self.level += 1
            
            self.progress_bar(self.xp, self.to_level_next)

            self.xp = self.xp - self.to_level_next
            self.to_level_next = int(self.to_level_next * 1.5)

            
            print(f"\n🎉 Congratulations! You've reached Level {self.level}!")
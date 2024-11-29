class Profile:
    def __init__(self, name, xp = 0, level = 1):
        self.name = name
        self.level = level
        self.xp = xp
        self.to_level_next = level * 25

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, XP: {self.xp}, Next Level: {self.to_level_next}"

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


        
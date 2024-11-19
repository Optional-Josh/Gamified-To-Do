class Profile:
    def __init__(self, name, level, xp):
        self.name = name
        self.level = level
        self.xp = xp
        self.to_level_next = level * 25

    def advance_level(self):
        level_next = round(self.to_level_next * 1.5)
        return f"Name: {self.name}\n Level: {self.level}\n XP: {self.xp} \n To Level up {level_next}"


        
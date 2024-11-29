from class_profile import Profile
from class_task import Task


# class Profile requires name, level and xp
# class Task requires name, priority, due date and points

def test(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')

if __name__ == "__main__":
    # test(name="Joshua", task="duty")
    person_one = Profile("Mr", 25)
    first_task = Task(person_one, "important", "today", 5, False)
    person_two = Profile("Mrs", 100, 1000)
    person_one.advance_level()
    first_task.compiler()
from class_profile import Profile
from class_task import Task


# class Profile requires name, level and xp
# class Task requires name, priority, due date and points

def test(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')

if __name__ == "__main__":
    # test(name="Joshua", task="duty")
    first_task = Task("record html", "important", "today", 5, False)
    print(first_task.compiler())
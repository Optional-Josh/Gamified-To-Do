from class_profile import Profile
from class_task import Task


# class Profile requires name, level and xp
# class Task requires name, priority, due date, points, and status

# def test_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key}: {value}')

if __name__ == "__main__":
    # test(name="Joshua", task="duty")
    person_one = Profile("Mr", 0, 1)
    # first_task = Task(person_one, "work out", "today", 25, True)
    # second_task = Task(person_one, "study", "today", 25, True)

    person_one.add_task("work out", "today", 25, True)
    person_one.add_task("train", "today", 25, True)
    print(person_one.task)


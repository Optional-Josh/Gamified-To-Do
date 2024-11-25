from class_profile import Profile
from class_task import Task

if __name__ == "__main__":
    profile_one = Profile("Joshua", 1, 5)
    print(profile_one.advance_level())

    task_one = Task("list all tasks", 10)
    task_two = Task("improve this program", 10)
    print(task_one.compiler())
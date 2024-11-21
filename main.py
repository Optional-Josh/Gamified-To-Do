from class_profile import Profile
from class_task import Task

if __name__ == "__main__":
    profile_one = Profile("Joshua", 1, 5)
    print(profile_one.advance_level())

    ideation = Task("list all tasks", 10)
    print(ideation.compiler())
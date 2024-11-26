from class_profile import Profile
from class_task import Task

def test(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')

if __name__ == "__main__":
    test(name="Joshua", task="duty")
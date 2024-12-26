import pandas as pd
from class_profile import Profile
from file_functions import append_dict_json, read_file, sort_json, load_file
from data_functions import convert_dataframe, dataframe_txt_styled

def menu_console():
    
    prompt = input("Please state your name\n")

    test_profile = Profile(prompt, 0, 1)

    help_menu = """
        Would you like to add, view, update or delete a record?
        Type 'add' to add record(s)
        Type 'view' to view records
        Type 'update' to update a record's status
        Type 'delete' to delete record(s)\n
        """
    
    while True:

        print(help_menu)
        prompt = input("Type your choice\n")
        lower_prompt = prompt.lower()

        if lower_prompt == 'add':
            i = int(input("How many records would you like to add?\n"))
            for record in range(0, i):
                test_profile.add_task()
            append_dict_json(test_profile.name, test_profile.task)

        elif lower_prompt == 'view':
            data = load_file(test_profile.name)
            df = convert_dataframe(data)
            print(df)

        elif lower_prompt == 'update':
            data = load_file(test_profile.name)
            df = convert_dataframe(data)

            prompt = int(input("Index of row to be marked complete\n"))
            df.loc[prompt, 'status'] = 'completed'
            print(df)

        elif lower_prompt == 'delete':
            data = load_file(test_profile.name)
            df = convert_dataframe(data)

            prompt = int(input("Index of row to be deleted\n"))
            df.drop(prompt, axis = 0, inplace=True)

            print(df)



        prompt = input("Continue to use? (Yes or No)\n")
        lower_prompt = prompt.lower()
        if lower_prompt == 'yes':
            continue
        else: 
            break



"""
 create a profile
 check if profile file exists or not

 once profile is made or logged in, 
 ask to add task, view, update or delete tasks
 then ask to check status of all tasks to be compiled to profile
 level up and then quit

"""

if __name__ == "__main__":
    menu_console()
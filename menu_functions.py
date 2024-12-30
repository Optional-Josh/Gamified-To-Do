import pandas as pd
import os
from class_profile import Profile
from file_functions import append_dict_json, read_file, sort_json, load_file, overwrite_dict_json
from data_functions import convert_dataframe

def user_login():

    while True:
        username = input("Please state your name\n")

        folder_path = "C:\\Users\\Administrator\\Desktop\\Entire Files\\Programming\\Self-Taught Work\\Gamified To Do"
        file_name = f"{username}.json"

        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            return username
        
def guide():
    print('''
        Category
        1 - Household, 2 - Work, 3 - Personal, 4 - Relationship
        Difficulty
        1 - Easy, 2 - Medium, 3 - Hard
        ''')

def menu_console(username):

    test_profile = Profile(username, 0, 1)

    help_menu = """
        Would you like to add, view, update or delete a record?
        Type 'add' to add record(s)
        Type 'view' to view records
        Type 'update' to update a record's status
        Type 'delete' to delete record(s)
        Type 'inspect' to check level, xp and progress to next level
        Type 'level' to level up if eligible
        """
    
    running = True
    while running:
        data = load_file(test_profile.name)

        print(help_menu)
        prompt = input("Type your choice\n")
        lower_prompt = prompt.lower()

        if lower_prompt == 'add':
            date_input = input("What are the date for this task(s) 'yyyy-mm-dd': ")
            i = int(input("How many records would you like to add?\n"))
            for record in range(0, i):
                guide()
                test_profile.add_task(date_input)
                print(f"Record added: {record+1}")
            append_dict_json(test_profile.name, test_profile.task)
            test_profile.task.clear()

        elif lower_prompt == 'view':

            headers = list(data[0].keys())

            column_widths = [max(len(str(row.get(col, ""))) for row in data + [dict(zip(headers, headers))])for col in headers]

            header_row = " | ".join(f"{col:<{w}}" for col, w in zip(headers, column_widths))
            print(header_row)
            print("-" * len(header_row))

            for row in data:
                print(" | ".join(f"{str(row.get(col, '')):<{w}}" for col, w in zip(headers, column_widths)))
            print(f"Total Number of Records: {len(data)}\n")


        elif lower_prompt == 'update':

            first_data = input("Description of record\n")
            second_data = input("Date of the record\n")
            record_found = False

            for row in data:
                if row['description'] == first_data and row['date'] == second_data:
                    row['status'] = 'completed'
                    record_found = True
                    break


            if record_found:
                overwrite_dict_json(test_profile.name, data)
                print("Record has been marked complete")
            else:
                print('Record not found')


        elif lower_prompt == 'delete':

            first_data = input("Description of record\n")
            second_data = input("Date of the record\n")
            initial_length = len(data)

            data = [row for row in data if not (row['description'] == first_data and row['date'] == second_data)]

            if len(data) < initial_length:
                overwrite_dict_json(test_profile.name, data)
                print("Record has been deleted")
            else:
                print("Record not found")

        elif lower_prompt == 'inspect':
            print(test_profile)
            test_profile.check_status(data)
            test_profile.progress_bar(test_profile.xp, test_profile.to_level_next)
            test_profile.level = 1
            test_profile.xp = 0
            test_profile.to_level_next = test_profile.level * 25
            print('\n')

        elif lower_prompt == 'level':
            test_profile.advance_level(data)
            test_profile.progress_bar(test_profile.xp, test_profile.to_level_next)
            test_profile.level = 1
            test_profile.xp = 0
            test_profile.to_level_next = test_profile.level * 25
            print('\n')
            


        if not input("Continue to use? (Yes or No)\n").lower() == 'yes':
            running = False


"""
 create a profile
 check if profile file exists or not

 once profile is made or logged in, 
 ask to add task, view, update or delete tasks
 then ask to check status of all tasks to be compiled to profile
 level up and then quit
"""

if __name__ == "__main__":
    info = user_login()
    menu_console(info)
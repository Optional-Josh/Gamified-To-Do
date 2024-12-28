import pandas as pd
from class_profile import Profile
from file_functions import append_dict_json, read_file, sort_json, load_file, overwrite_dict_json
from data_functions import convert_dataframe, dataframe_txt_styled

def menu_console():
    
    prompt = input("Please state your name\n")
    running = True

    test_profile = Profile(prompt, 0, 1)

    help_menu = """
        Would you like to add, view, update or delete a record?
        Type 'add' to add record(s)
        Type 'view' to view records
        Type 'update' to update a record's status
        Type 'delete' to delete record(s)\n
        """
    
    while running:

        print(help_menu)
        prompt = input("Type your choice\n")
        lower_prompt = prompt.lower()

        if lower_prompt == 'add':
            i = int(input("How many records would you like to add?\n"))
            for record in range(0, i):
                test_profile.add_task()
                print(f"Record added: {record+1}")
            append_dict_json(test_profile.name, test_profile.task)

        elif lower_prompt == 'view':
            data = load_file(test_profile.name)

            headers = list(data[0].keys())

            column_widths = [max(len(str(row.get(col, ""))) for row in data) for col in headers]

            header_row = " | ".join(f"{col:<{w}}" for col, w in zip(headers, column_widths))
            print(header_row)
            print("-" * len(header_row))

            for row in data:
                print(" | ".join(f"{str(row.get(col, '')):<{w}}" for col, w in zip(headers, column_widths)))
            print('\n')


        elif lower_prompt == 'update':
            data = load_file(test_profile.name)

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
            data = load_file(test_profile.name)

            first_data = input("Description of record\n")
            second_data = input("Date of the record\n")
            initial_length = len(data)

            data = [row for row in data if not (row['description'] == first_data and row['date'] == second_data)]

            if len(data) < initial_length:
                overwrite_dict_json(test_profile.name, data)
                print("Record has been deleted")
            else:
                print("Record not found")


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
    menu_console()
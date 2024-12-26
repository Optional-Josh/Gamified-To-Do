from class_profile import Profile
from file_functions import append_dict_json, read_file, sort_json, load_file
from data_functions import convert_dataframe, dataframe_txt_styled

# class Profile requires name, level and xp
# class Profile has a method to add tasks which is stored in a dictionary and appended to list
# function dataframe_txt_styled has dataframe and profile name as parameters

# method to add task requires description, date, points, and status as parameters


if __name__ == "__main__":
    main_prof = Profile("Joshua", 0, 1)
    prof_name = main_prof.name

    # for i in range(0,10):
    #     main_prof.add_task()
    #     print(f"Number of entries: {i+1}")
    #     if i == 9: 
    #         data = main_prof.task
    #         append_dict_json(prof_name, data)
    temp_data = load_file(prof_name)
    df_data = convert_dataframe(temp_data)
    main_prof.advance_level(temp_data)



    



from class_profile import Profile
from file_functions import append_dict_json, read_file, sort_json, load_file
from data_functions import convert_dataframe, dataframe_txt_styled

# class Profile requires name, level and xp
# class Profile has a method to add tasks which is stored in a dictionary and appended to list
# function dataframe_txt_styled has dataframe and profile name as parameters

# method to add task requires description, date, points, and status as parameters


if __name__ == "__main__":
    person_one = Profile("Jake", 0, 1)

    # json_data = load_file(person_one.name)
    # dataframe = convert_dataframe(json_data)
    # print(dataframe_txt_styled(dataframe, person_one.name))
    
    person_one.add_task("record video", "today", 25, True)
    person_one.add_task("journal", "today", 25, False)
    person_one.add_task("program", "today", 25, False)
    person_one.add_task("study", "today", 25, False)
    person_one.add_task("edit video", "today", 25, False)
    # append_dict_json(person_one.name, person_one.task)
    # read_file(person_one.name)
    data = load_file(person_one.name)
    dataframe_data = convert_dataframe(data)
    dataframe_txt_styled(dataframe_data, person_one.name)


    # person_one.check_status()
    # person_one.advance_level()



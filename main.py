from class_profile import Profile
from file_functions import append_dict_json, read_file, sort_json, load_file
from data_functions import convert_dataframe, dataframe_txt_styled

# class Profile requires name, level and xp
# class Profile has a method to add tasks which is stored in a dictionary and appended to list
# function dataframe_txt_styled has dataframe and profile name as parameters

# method to add task requires description, due date, points, and status as parameters


if __name__ == "__main__":
    person_one = Profile("Jake", 0, 1)

    json_data = load_file(person_one.name)
    dataframe = convert_dataframe(json_data)
    print(dataframe_txt_styled(dataframe, person_one.name))
    



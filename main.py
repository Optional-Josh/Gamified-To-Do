import os
import pandas as pd
from class_profile import Profile
from file_functions import append_dict_json, read_file, sort_json, load_file
from data_functions import convert_dataframe

# class Profile requires name, level and xp
# class Profile has a method to add tasks which is stored in a dictionary and appended to list
# function dataframe_txt_styled has dataframe and profile name as parameters

# method to add task requires description, date, points, and status as parameters

if __name__ == "__main__":
    joshua = Profile("Joshua", 0, 1)
    data = load_file(joshua.name)
    joshua.advance_level(data)
    joshua.progress_bar(joshua.xp, joshua.to_level_next)
    
    



    



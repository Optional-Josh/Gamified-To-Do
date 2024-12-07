import json

# profile arguments for each file function refers to name argument upon creating class
# converts the json into readable python format
def load_file(profile):
    with open(f'{profile}.json', 'r') as read_file:
        data = json.load(read_file)
    return data

# takes content of json to be a string for readable format
def read_file(profile):
    with open(f'{profile}.json', 'r') as read_file:
        data = json.load(read_file)
        formatted_data = (json.dumps(data, indent=2))
    return formatted_data

# adds data into json file and validates contents of json has a list inside 
# wherein extend will add elements to a list individually
# while append adds elements as a single element
def append_dict_json(profile, content):
    try:
        with open(f"{profile}.json", "r") as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                data = data
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if isinstance(content, list):
        data.extend(content)
    else:
        data.append(content)

    with open(f"{profile}.json", "w") as json_file:
        json.dump(data, json_file, indent = 2)

# function that separates the task dictionaries based on their status of completion of True/False
def sort_json(datas):

    # list comprehension to complete and incomplete tasks to be sorted
    complete_tasks = [task for task in datas if task["status"] is True]
    incomplete_tasks = [task for task in datas if task["status"] is False]

    return f"Completed Tasks: {complete_tasks}\nIncomplete Tasks: {incomplete_tasks}"


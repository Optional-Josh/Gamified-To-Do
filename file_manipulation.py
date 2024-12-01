import json

def add_to_file(content):
    with open('tasks.json', 'a') as appended_file:
        json.dump(content, appended_file, indent=2)

def read_file():
    with open('tasks.json', 'r') as read_file:
        data = json.load(read_file)
        formatted_data = (json.dumps(data, indent=2))
    return formatted_data

def append_dict_json(content):
    try:
        with open("tasks.json", "r") as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                data = data
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(content)

    with open("tasks.json", "w") as json_file:
        json.dump(data, json_file, indent = 2)
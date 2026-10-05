import json
def get_json_data(key,path):
    with open(path, "r") as config_file:
        config = json.load(config_file)
        value = config[key]
    return value
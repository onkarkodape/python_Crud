import json
import os.path


def read_file():
    base_dir =os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    json_file_path = os.path.join(base_dir,'resources\\random_json.json')

    with open(json_file_path,'r') as f :
        content = json.loads(f.read())
        return content
import json
json_path = 'python50k_eval.json'


with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
print(data.items())

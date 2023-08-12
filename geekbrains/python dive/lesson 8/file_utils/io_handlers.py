import json
import csv
import pickle

def save_to_json(data, filename="output.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_csv(data, filename="output.csv"):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['type', 'name', 'parent_dir', 'size'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def save_to_pickle(data, filename="output.pkl"):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

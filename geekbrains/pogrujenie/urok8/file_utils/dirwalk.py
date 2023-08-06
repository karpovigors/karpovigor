import os

def recursive_dir_walk(dir_path, parent_dir=None):
    items = []

    for item_name in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item_name)
        if os.path.isfile(item_path):
            items.append({
                'type': 'file',
                'name': item_name,
                'parent_dir': parent_dir,
                'size': os.path.getsize(item_path)
            })
        elif os.path.isdir(item_path):
            dir_size = sum(d['size'] for d in recursive_dir_walk(item_path, item_name))
            items.append({
                'type': 'directory',
                'name': item_name,
                'parent_dir': parent_dir,
                'size': dir_size
            })
            items.extend(recursive_dir_walk(item_path, item_name))
    
    return items

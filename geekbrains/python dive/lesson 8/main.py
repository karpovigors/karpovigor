from file_utils import recursive_dir_walk, save_to_json, save_to_csv, save_to_pickle

data = recursive_dir_walk('./')
save_to_json(data)
save_to_csv(data)
save_to_pickle(data)

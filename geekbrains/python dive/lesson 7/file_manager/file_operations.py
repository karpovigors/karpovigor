import os

def rename_files_in_directory(new_name, digit_count, source_ext, target_ext, name_range, directory='.'):
    """
    Групповое переименование файлов в указанной директории.
    
    :param new_name: новое имя файла
    :param digit_count: количество цифр в порядковом номере
    :param source_ext: расширение исходных файлов
    :param target_ext: расширение после переименования
    :param name_range: диапазон сохраняемого оригинального имени
    :param directory: директория, в которой находятся файлы для переименования. По умолчанию - текущая директория.
    """
    
    files = [f for f in os.listdir(directory) if f.endswith(source_ext)]
    
    counter = 1
    for file in files:
        old_name_base = os.path.splitext(file)[0]
        new_name_base = old_name_base[name_range[0]:name_range[1]] + new_name + str(counter).zfill(digit_count)
        
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name_base + target_ext)
        
        os.rename(old_path, new_path)
        counter += 1

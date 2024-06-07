import os
import time
import fnmatch
import shutil
import glob

base_path = os.path.expanduser('~')  
sub_directory = 'Documents/Company_specific_resumes'  
new_folder_name = '' 

def move_file(source_path, destination_path):
    try:
        # Move the file
        shutil.move(source_path, destination_path)
        print(f"File moved from '{source_path}' to '{destination_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_recent_files(directory, pattern, lookback_seconds):
    current_time = time.time()
    recent_files = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # Check if it's a file (not a directory) and if it matches the pattern
        if os.path.isfile(filepath) and fnmatch.fnmatch(filename, pattern):
            # Get the file's modification time
            file_ctime = os.path.getctime(filepath)

            if current_time - file_ctime <= lookback_seconds:
                recent_files.append(filename)

    return recent_files


def check_files_with_pattern(folder_path, pattern):
    search_pattern = os.path.join(folder_path, pattern)
    matching_files = glob.glob(search_pattern)
    current_time = time.time()
    # Filter files based on created time
    matching_files = [file for file in matching_files if current_time - os.path.getctime(file) <= 10000]
    return matching_files



def split_filename(filename):
    # Split the filename based on the last underscore
    if '_' in filename:
        extract_info = filename.split("_")
        print(extract_info)
        
        # Split the filename into two parts
        part1 = extract_info[0]+"_"+extract_info[1]
        part2 = extract_info[2] #role_name
        part3 = extract_info[3] #company
        return part1, part2, part3
    else:
        return filename, ''
    
def create_new_folder(base_path, sub_directory, new_folder_name):
    full_path_1 = os.path.join(base_path, sub_directory, new_folder_name)
    full_path_2 = os.path.join(base_path, sub_directory, new_folder_name)
    
    try:
        # Create the directory
        os.makedirs(full_path_1, exist_ok=True)
        print(f"Directory '{new_folder_name}' created at '{os.path.join(base_path, sub_directory)}'")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    downloads_path = os.path.join('/Users/jyothivaidyanathan/Downloads/')
    pattern = '*<YourName>_Resume*'  
    lookback_seconds = 60
    check_interval_seconds = 30

    while True:
        recent_files = get_recent_files(downloads_path, pattern, lookback_seconds)
        if recent_files:
            print(f"Recent files matching '{pattern}' downloaded in the last {lookback_seconds} seconds:")
            for file in recent_files:
                print(file)
                for file in recent_files:
                    part1, part2, part3 = split_filename(file)
                    extract_file_extension=part3.split(".")
                    part3=extract_file_extension[0]
                    extension=extract_file_extension[1]
                    print(f"Original: {file}, Part 1: {part1}, Part 3: {part3}")
                    new_folder_name=part3+"/"+part2
                    #new_subfolder_name=part2
                    create_new_folder(base_path, sub_directory, new_folder_name)
                    print("folder created")
                    source_path = os.path.join('/Users/jyothivaidyanathan/Downloads', file)
                    to_save_in=base_path+"/"+sub_directory+"/"+new_folder_name+"/"
                    destination_path = os.path.join(to_save_in, part1+"."+extension)
                    move_file(source_path, destination_path)
        else:
            print(f"No recent files matching '{pattern}' in the last {lookback_seconds} seconds.")
        time.sleep(check_interval_seconds)

if __name__ == "__main__":
    main()

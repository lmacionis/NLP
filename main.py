import os


directory = "data"

# Creating directory for data storage.
def create_dir_data():
    try:
        os.mkdir(directory)
        print(f"Directory {directory} created successfully.")
    except FileExistsError:
        print(f"Directory {directory} already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

create_dir_data()
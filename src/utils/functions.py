import os

def add_dataset_file_path(dirname_dataset, file_name):
  if not (dirname_dataset) :
    raise ValueError("DATASET_FOLDER_PATH is not found. Please set the environment variables in .env")
  
  return os.path.join(dirname_dataset, file_name)
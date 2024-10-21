from data import DataHandler
from dotenv import load_dotenv
import os

from constants import *
from utils import create_file_dict

load_dotenv()

dirname = os.getenv('DATASET_FOLDER_PATH')

if not dirname:
  raise ValueError("DATASET_FOLDER_PATH is not found. Please set the environment variables in .env")

# User Listening Histories Dataset
listening_file = create_file_dict(dirname, path_listening_history, path_listening_history_parquet)
listening_columns = ['user_id', 'timestamp', 'artist_id', 'artist_name', 'track_id', 'track_name']
skiprows = [2120260-1, 2446318-1, 11141081-1, 11152099-1, 11152402-1, 11882087-1, 12902539-1, 12935044-1, 17589539-1]
attributes = {'separator': '\t', 'header': None}

listening_history = DataHandler(listening_file, listening_columns, skiprows, attributes)

# User Profiles Dataset
user_file = create_file_dict(dirname, path_user_data, path_user_data_parquet)
user_columns = ['user_id', 'gender', 'age', 'country', 'signup']

user_profile = DataHandler(user_file, user_columns, [], attributes)

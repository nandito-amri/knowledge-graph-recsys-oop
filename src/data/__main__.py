from . import data
from utils.constants import *
from utils.functions import add_dataset_file_path

# A DataHandler Parameter should include data_name, file_path, file_path_save, column, skiprows, and attributes

listening_history_params = {
  'data_name': 'Listening History',
  'file_path': add_dataset_file_path(dirname_dataset, path_listening_history),
  'file_path_save': add_dataset_file_path(dirname_dataset, path_listening_history_parquet),
  'columns': ['user_id', 'timestamp', 'artist_id', 'artist_name', 'track_id', 'track_name'],
  'skiprows': [2120260-1, 2446318-1, 11141081-1, 11152099-1, 11152402-1, 11882087-1, 12902539-1, 12935044-1, 17589539-1],
  'attributes': {'separator': '\t', 'header': None}
}

user_profile_params = {
  'data_name': 'User Profile',
  'file_path': add_dataset_file_path(dirname_dataset, path_user_data),
  'file_path_save': add_dataset_file_path(dirname_dataset, path_user_data_parquet),
  'columns': ['user_id', 'gender', 'age', 'country', 'signup'],
  'skiprows': [],
  'attributes': {'separator': '\t', 'header': 0}
}

listening_history = data.DataHandler(
  data_name=listening_history_params['data_name'],
  file_path=listening_history_params['file_path'],
  file_path_save=listening_history_params['file_path_save'],
  columns=listening_history_params['columns'],
  skiprows=listening_history_params['skiprows'],
  attributes=listening_history_params['attributes']
)

user_profile = data.DataHandler(
  data_name=user_profile_params['data_name'],
  file_path=user_profile_params['file_path'],
  file_path_save=user_profile_params['file_path_save'],
  columns=user_profile_params['columns'],
  skiprows=user_profile_params['skiprows'],
  attributes=user_profile_params['attributes']
)

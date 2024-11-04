from . import data_preprocessing
from utils.constants import *
from utils.functions import add_dataset_file_path

listening_history = data_preprocessing.DataFrame_.from_parquete(
  file_path=add_dataset_file_path(dirname_dataset, path_listening_history_parquet),
  columns=['user_id', 'timestamp', 'artist_id', 'artist_name', 'track_id', 'track_name']
)

user_profile = data_preprocessing.DataFrame_.from_parquete(
  file_path=add_dataset_file_path(dirname_dataset, path_user_data_parquet),
  columns=['user_id', 'gender', 'age', 'country']
)


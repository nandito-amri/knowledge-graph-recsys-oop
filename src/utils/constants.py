import os
from dotenv import load_dotenv

load_dotenv()

dirname_dataset = os.getenv('DATASET_FOLDER_PATH')

path_listening_history = "userid-timestamp-artid-artname-traid-traname.tsv"

path_user_data = "userid-profile.tsv"

path_listening_history_parquet = "listening_history.snappy.parquet"

path_user_data_parquet = "user_data.snappy.parquet"

path_graphml = 'knowledge_graph.graphml'
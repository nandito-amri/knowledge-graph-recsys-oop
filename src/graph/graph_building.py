from sklearn.preprocessing import LabelEncoder
import pandas as pd

from . import datasets
from . import graph
from utils.constants import *
from utils.functions import add_dataset_file_path

selected_users = datasets.listening_history.df['user_id'].unique()[::20]
listening_history_dataset = datasets.listening_history.df.loc[datasets.listening_history.df['user_id'].isin(selected_users)].sort_values(['user_id'])
user_profile_dataset = datasets.user_profile.df.loc[datasets.user_profile.df['user_id'].isin(selected_users)].sort_values(['user_id'])

# Data Cleaning
listening_history_dataset.drop(['timestamp'], inplace=True, axis=1)

user_profile_dataset['background'] = user_profile_dataset.apply(lambda row: f"{row['gender']} - {row['age']} - {row['country']}", axis=1)
user_profile_dataset['background_id'] = pd.factorize(user_profile_dataset['background'])[0]
user_profile_dataset['background_id'] = 'background_' + user_profile_dataset['background_id'].astype(str)

# Manipulate Columns For 'listened_to' Relation
relation_listened_to = listening_history_dataset.drop(columns=['artist_name', 'track_id', 'track_name'])
relation_listened_to.dropna(inplace=True)
relation_listened_to.drop_duplicates(inplace=True, ignore_index=True)
relation_listened_to.rename({'user_id': 'head', 'artist_id': 'tail'}, axis=1, inplace=True)
relation_listened_to['relation'] = 'listened_to'

# Manipulate Columns For 'played' Relation
relation_played = listening_history_dataset.drop(columns=['artist_id', 'artist_name', 'track_name'])
relation_played.dropna(inplace=True)
relation_played.drop_duplicates(inplace=True, ignore_index=True)
relation_played.rename({'user_id': 'head', 'track_id': 'tail'}, axis=1, inplace=True)
relation_played['relation'] = 'played'

# Manipulate Columns For 'sing' Relation
relation_sing = listening_history_dataset.drop(columns=['user_id', 'artist_name', 'track_name'])
relation_sing.dropna(inplace=True)
relation_sing.drop_duplicates(inplace=True, ignore_index=True)
relation_sing.rename({'artist_id': 'head', 'track_id': 'tail'}, axis=1, inplace=True)
relation_sing['relation'] = 'sing'

# Manipulate Columns For 'has_background' Relation
relation_has_background = user_profile_dataset.drop(['gender', 'age', 'country', 'background'], axis=1)
relation_has_background.rename({'user_id': 'tail', 'background_id': 'head'}, axis=1, inplace=True)
relation_has_background = relation_has_background.iloc[:, [1, 0, 2]]
relation_has_background['relation'] = 'has_background'

# Concatinate 4 Relation for Creating List of Edges of Knowledge Graph
graph_data = [relation_has_background, relation_listened_to, relation_played, relation_sing]
edges_list = pd.concat(graph_data, ignore_index=True)
edges_list.dropna(inplace=True)

graph = graph.Graph(edges_list, ['head', 'tail', 'relation'], add_dataset_file_path(dirname_dataset, path_graphml))
graph.save_graph()

triplets = graph.get_triplets()
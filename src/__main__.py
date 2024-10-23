import embedding_packages.graph_embedding as embedder

# Triplets Example
import random
users = [f"user_{i}" for i in range(1, 6)]  # 5 users
artists = [f"artist_{i}" for i in range(1, 6)]  # 5 artists
tracks = [f"track_{i}" for i in range(1, 6)]  # 5 tracks

# Relations
relations = ['sing', 'listened_to', 'played']

triplets = []

for _ in range(7):
    artist = random.choice(artists)
    track = random.choice(tracks)
    triplets.append((artist, 'sing', track))

for _ in range(7):
    user = random.choice(users)
    track = random.choice(tracks)
    triplets.append((user, 'listened_to', track))

for _ in range(6):
    user = random.choice(users)
    artist = random.choice(artists)
    triplets.append((user, 'played', artist))


graph = embedder.GraphEmbedding(triplets, dimension=10, batch_size=5)

entities, loss = graph.embedding_learning(epochs=100, margin=1, n_neg_triplet=4)

import numpy as np
rng = np.random.default_rng()

from .transm import TransM

class GraphEmbedding:
  def __init__(self, triplets, dimension=30, batch_size=200):
    self._triplets = triplets
    self._dimension = dimension
    self._batch_size = batch_size
    self.entities = self._get_entities()
    self.relations = self._get_relations()
    self.valid_triplets = self._split_dataset()
    self.relation_weights = self._get_mapping_degree()

  def _initialize_vector(self):    # Initializing Vector
    limit = 6 / np.sqrt(self._dimension)
    return rng.uniform(-limit, limit, self._dimension)

  def _get_entities(self):    # Setting and Normalizing Entities of Graph
    entity_names = set([str(triplet[0]) for triplet in self._triplets] + [str(triplet[2]) for triplet in self._triplets])
    entity_embeddings = {name: self._initialize_vector() for name in entity_names}
    return {name: self._normalize_vector(embedding) for name, embedding in entity_embeddings.items()}

  def _get_relations(self):    # Setting and Normalizing Relations of Graphs
    relation_names = set([triplet[1] for triplet in self._triplets])
    relation_embeddings = {name: self._initialize_vector() for name in relation_names}
    return {name: self._normalize_vector(embedding) for name, embedding in relation_embeddings.items()}

  def _normalize_vector(self, vector):    # Normalizing vector
    norm = np.linalg.norm(vector)
    if norm == 0:
      return vector
    return vector / norm
    
  def _get_mapping_degree(self):    # Weighting Relation
    relation_weights = dict()

    for relation in self.relations:
      num_triplets = 0
      distinc_heads = set({})
      distinc_tails = set({})
      for triplet in self._triplets:
        if triplet[1] == relation:
          num_triplets += 1
          distinc_heads.add(triplet[0])
          distinc_tails.add(triplet[2])
      weight = 1 / np.log10((num_triplets / len(distinc_heads)) + (num_triplets / len(distinc_tails)))
      relation_weights[relation] = weight

    return relation_weights

  def _group_by_relation(self):
    grouped_triplets = {relation: [] for relation in self.relations}
    for triplet in self._triplets:
      _, relation, _ = triplet
      grouped_triplets[relation].append(triplet)
    
    return list(grouped_triplets.values())

  # Spliting Dataset
  def _split_dataset(self):
    split_batches = []
    for group in self._group_by_relation():
      for i in range(0, len(group), self._batch_size):
        split_batches.append(group[i:i + self._batch_size])

    return split_batches
  
  def embedding_learning(self, learning_rate=0.1, margin=0.5, epochs=50, n_neg_triplet=2):
    self.model = TransM(
      self.valid_triplets, 
      self.entities, 
      self.relations, 
      self.relation_weights, 
      learning_rate, 
      margin, epochs, 
      n_neg_triplet)
    self.model.embedding_training()

    return self.entities, self.model.get_loss()
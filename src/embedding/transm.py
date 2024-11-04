import numpy as np
rng = np.random.default_rng()

class TransM:
  def __init__(self, triplets, entities, relations, relation_weights, learning_rate, margin, epochs, n_neg_triplets):
    self.triplets = triplets
    self.entities = entities
    self.relations = relations
    self.relation_weights = relation_weights
    self._learning_rate = learning_rate
    self._margin = margin
    self._epochs = epochs
    self._n_neg_triplets = n_neg_triplets
    self.loss = 0

  def _generate_negative_triplet(self, head, relation, tail, corrupt_tail=True):   # Generating n-negative triplets
    if corrupt_tail:
      corrupted_tail = tail
      while corrupted_tail == tail: 
        corrupted_tail = rng.choice(list(self.entities.keys()))
      negative_triplet = (head, relation, corrupted_tail)
    else:
      corrupted_head = head
      while corrupted_head == head:  
        corrupted_head = rng.choice(list(self.entities.keys()))
      negative_triplet = (corrupted_head, relation, tail)

    return negative_triplet

  def _get_score(self, head, relation, tail):   # Scoring function
    l2_distance = np.linalg.norm(self.entities[head] + self.relations[relation] - self.entities[tail])
    return self.relation_weights[relation] * l2_distance

  def _get_loss(self, pos_score, neg_score):    # Loss function
    return max(0, self._margin + pos_score - neg_score)

  def _calculate_gradient(self, head, relation, tail):    # Calculating gradient for a vector
    return np.array([(2 * self.relation_weights[relation] * (self.entities[head][i] + self.relations[relation][i] - self.entities[tail][i])) for i in range(len(self.entities[head]))])
  
  def _normalize_vector(self, vector):    # Normalizing vector
    norm = np.linalg.norm(vector)
    if norm == 0:
      return vector
    return vector / norm
  
  def embedding_training(self):    # Training Process
    total_loss = 0
    for index, triplet_batches in enumerate(self.triplets):
      batch_loss = 0
      for epoch in range(self._epochs):
        batch_loss = 0
        for valid_triplet in triplet_batches:
          head, relation, tail = valid_triplet

          negative_triplet_tail = [self._generate_negative_triplet(head, relation, tail) for _ in range(int(self._n_neg_triplets / 2))]
          negative_triplet_head = [self._generate_negative_triplet(head, relation, tail, False) for _ in range(int(self._n_neg_triplets /   2))]
          negative_triplets = negative_triplet_head + negative_triplet_tail

          positive_score = self._get_score(head, relation, tail)
          negative_score = [self._get_score(negative_triplets[i][0], negative_triplets[i][1], negative_triplets[i][2]) for i in range(len(negative_triplets))]

          loss = sum(self._get_loss(positive_score, negative_score[i]) for i in range(len(negative_score)))
          batch_loss += loss

          if loss > 0:
            gradient = self._calculate_gradient(head, relation, tail)
            self.entities[head] -= self._learning_rate * gradient
            self.entities[tail] += self._learning_rate * gradient

            self.entities[head] = self._normalize_vector(self.entities[head])
            self.entities[tail] = self._normalize_vector(self.entities[tail])

        if batch_loss == 0:
          print(f'Epoch {epoch+1}/{self._epochs}, Batch: {index+1}, Loss: {batch_loss} - Training stopped early.')
          break

        if epoch == self._epochs - 1:
          print(f'Epoch {epoch+1}/{self._epochs}, Batch: {index+1}, Loss: {batch_loss} - Training finished.')


      total_loss += batch_loss

    print(f'✅ Embedding Completed!, Loss: {total_loss}, Average Loss: {total_loss / len(self.triplets)}')

    self.loss = total_loss / len(self.triplets)

  def get_loss(self):
    return self.loss
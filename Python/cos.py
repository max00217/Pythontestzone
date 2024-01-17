import numpy as np

def cos_similarity(v1, v2):
  v1 = np.array(v1) # vector 1
  v2 = np.array(v2) # vector 2
    
  dp = np.dot(v1, v2) # dot product
  n_v1 = np.linalg.norm(v1) # norm of vector 1
  n_v2 = np.linalg.norm(v2) # norm of vector 2
    
  cos_sim = dp / (n_v1 * n_v2) # cosine similarity
  cos_sim = round(cos_sim, 3)
    
  return cos_sim
  
v1 = [1, 1, 0, 1, 1, 2, 1, 0, 1, 1] # vector 1
v2 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0] # vector 2
cos_sim = cos_similarity(v1, v2)
print(f'Cosine similarity: {cos_sim}')


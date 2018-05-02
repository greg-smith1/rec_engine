import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors


class UserRecommendationSystem(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def near_neighbors(self):
        model = NearestNeighbors(metric='cosine', algorithm='brute')
        model.fit(self.matrix)

        return model

    def rec_by_users(self, model, index):
        matrix = self.matrix
        #query_index = np.random.choice(matrix.shape[0])
        query_index = index
        distances, indices = model.kneighbors(matrix.iloc[query_index, :].values.reshape(1, -1), n_neighbors = 6)

        for i in range(0, len(distances.flatten())):
            if i == 0:
                print('Recommendations for {0}:\n'.format(matrix.index[query_index]))
            else:
                print('{0}: {1}, with distance of {2}:'.format(i, matrix.index[indices.flatten()[i]], distances.flatten()[i]))
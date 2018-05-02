
import pandas as pd
import time
from flask import current_app
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel



class RecommendationSystem(object):

    def __init__(self, data_source):
        self.data = pd.read_csv(data_source)

    def populate(self):
        df = self.data
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
        tfidf_matrix = tf.fit_transform(df['review/text'])

        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
        return cosine_similarities

    def generate_similarity(self, matrix):
        df = self.data
        with open('similar_beers_matrix.csv', 'w+') as beer_matrix:
            beer_matrix.write('self_id,id1,id2,id3,id4,id5,id6,id7,id8\n')
            for index, row in df.iterrows():
                similar_indices = matrix[index].argsort()[:-10:-1]
                similar_items = [(matrix[index][i], df['beer/beerId'][i]) for i in similar_indices]
                new_items = sum(similar_items[:], ())
                self_score, self_id, score1, id1, score2, id2, score3, id3, score4, id4, score5, id5, score6, id6, score7, id7, score8, id8 = new_items
                #beer_name = df[(df['beer/beerId'] == self_id)][:1]['beer/name'].item()
                new_line = "{0},{1},{2},{3},{4},{5},{6},{7},{8}".format(self_id,id1,id2,id3,id4,id5,id6,id7,id8)
                beer_matrix.write('{new_line}\n'.format(new_line=new_line))
            

        
        return new_items, new_line

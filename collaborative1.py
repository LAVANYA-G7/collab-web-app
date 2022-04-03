#Collaborative

import pandas as pd
import pickle

item_similarity_df = pickle.load(open('C:/Users/lenovo/Downloads/collab_trained_model.sav', 'rb'))

def get_similar_products(product_name, user_rating):
  similar_score=item_similarity_df[product_name]*(user_rating-2.5)
  similar_score=similar_score.sort_values(ascending=False)
  return similar_score

example=[("B00001P4ZH", 4),("B00004T8R2", 5),("B00004ZCC1", 3),("B00004ZCJI", 1),("B00004ZCJJ", 2)]
similar_products=pd.DataFrame()
for product, rating in example:
  similar_products=similar_products.append(get_similar_products(product, rating),ignore_index=True)
similar_products.head()
print(similar_products.sum().sort_values(ascending=False).head())



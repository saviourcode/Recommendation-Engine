#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import pickle
from sklearn.impute import SimpleImputer


# In[17]:


# Reading dataframe
df = pd.read_csv('netflix_titles.csv')

# Replacing NaN values of columns Date added and Rating
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer.fit(df.iloc[:,6:9])
df.iloc[:,6:9] = imputer.transform(df.iloc[:,6:9])

# Removing Irrelevant Columns
df.drop(['show_id', 'description', 'date_added', 'release_year', 'duration'], axis=1, inplace= True)

# Flattening the dataset
single_col = ['type', 'rating']
multi_col = ['director', 'cast', 'country', 'listed_in']
for i in multi_col:
    df[i] = df[i].apply(lambda x: str(x).replace(' ','').split(','))

# Converting title to lowercase
df['title'] = df['title'].str.lower()

# Creating binary Matrix
single_col = ['type', 'rating']
multi_col = ['director', 'cast', 'country', 'listed_in']

binary_df = pd.DataFrame({'Index':df.index})
binary_df = binary_df.set_index('Index')

# Single Value
for i in single_col:
    for j in df[i].unique():
        binary_df[j] = 0
for i in range(len(df)):
    row = df.index[i]
    for j in single_col:
        value = df[j][row]
        binary_df.loc[row,value] = 1

# Multiple Value
for i in multi_col:
    unique_list = []
    for j in df[i]:
        for x in j:
            unique_list.append(x)
    unique_set = set(unique_list)

    for value in unique_set:
        binary_df[value] = 0

for i in range(len(df)):
    row = df.index[i]
    for j in multi_col:
        for value in df[j][row]:
            binary_df.loc[row,value] = 1

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(binary_df, binary_df)

# Construct a reverse map of indices and movie titles
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

class Recommender:

    def get_recommendation(self, title):
        try:
            title = title.lower()
            row_index = indices[title]
            sim_scores = list(enumerate(cosine_sim[row_index]))
            sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)

            sim_scores = sim_scores[1:11]

            movie_indices = [i[0] for i in sim_scores]

            return df.iloc[movie_indices]['title'].str.upper()
        except:
            return 'Movie/ TV Series not found. Please enter a different title.'


# In[18]:


movie = Recommender()


# In[23]:


# Serializing
with open('movie.pkl', 'wb') as handle:
    pickle.dump(movie, handle, pickle.HIGHEST_PROTOCOL)


# In[ ]:





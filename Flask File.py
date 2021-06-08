#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
# from Recommender import RecommenderDS


# In[ ]:


from App import Recommender


# In[ ]:


app = Flask(__name__)
CORS(app)
@app.route("/recommend/", methods=['GET'])
def recommend():
    print('Inside Recommend')
    title = request.args.get('title')
    print(title)
    result = Recommender().get_recommendation(title)
    print(list(result))
    result_dict = {'Recommended': list(result)}
    return jsonify(result_dict)

@app.route("/",methods=['GET'])
def default():
    print('Entering Default')
    return "<h1> Welcome to Netflix Recommendation Engine <h1>"


# In[ ]:


if __name__ == "__main__":
    app.run() 


# In[ ]:





# In[ ]:





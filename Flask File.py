from flask import Flask, render_template
from flask import render_template_string

import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from App import Recommender

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
    #return jsonify(result_dict)
    return render_template_string('''
    <table>
            <tr>
                <td> Title </td> 
            </tr>

    {% for title in result.items() %}

            <tr>
                <td>{{ title }}</td> 
            </tr>

    {% endfor %}


    </table>
''', result=result)

@app.route("/",methods=['GET'])
def default():
   return render_template('index.html')


if __name__ == "__main__":
    app.run() 


from flask import Flask, render_template, flash, redirect, url_for
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key for flashing messages

# Your existing functions go here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    predict()
    return render_template('predict.html')

@app.route('/actual')
def actual():
    actual()
    return render_template('actual.html')

@app.route('/state_analysis/<state>')
def state_analysis(state):
    applot(state)
    return render_template('state_analysis.html')

if __name__ == '__main__':
    app.run(debug=True)

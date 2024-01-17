from flask import Flask, render_template, request
#import FinalLearnM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    state = request.form.get('state')
    result_data = get_result_data(state)
    return render_template('result.html', state=state, result_data=result_data)

def get_result_data(state):
    # Call the appropriate functions from FinalLearnM and return the result data
    # Example: result_data = FinalLearnM.some_function(state)
    return "Replace this with the actual result data"

if __name__ == '__main__':
    app.run(debug=True)

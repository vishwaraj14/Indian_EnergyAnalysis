from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from PIL import Image, ImageTk
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Sample dataset (replace this with the actual path to your dataset)
dataset_path = 'D:/final year project/Analysis-of-Energy-Consumption-in-India-SDL-Project-master/Book1.csv'
df = pd.read_csv(dataset_path)

def plot_pie_chart(state, year):
    data = df[(df['State'] == state) & (df['Year'] == year)].iloc[:, 1:7]
    labels = data.columns
    values = data.iloc[0].values

    # Set the backend to 'Agg'
    plt.switch_backend('Agg')

    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'{state} Energy Composition ({year})')

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    plt.close()

    # Encode the image to base64 for displaying in HTML
    encoded_image = base64.b64encode(image_stream.read()).decode('utf-8')
    return encoded_image

def plot_bar_chart(state, year):
    data = df[(df['State'] == state) & (df['Year'] == year)].iloc[:, 1:7]
    labels = data.columns
    values = data.iloc[0].values

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color=['red', 'blue', 'green', 'orange', 'purple', 'brown'])
    plt.title(f'{state} Energy Composition ({year})')
    plt.xlabel('Energy Source')
    plt.ylabel('Energy (in GWh)')
    plt.show()

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    plt.close()

    # Encode the image to base64 for displaying in HTML
    encoded_image = base64.b64encode(image_stream.read()).decode('utf-8')
    return encoded_image


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    state = request.form.get('state')
    year = int(request.form.get('year'))

    # Check if the state exists in the dataset
    if state not in df['State'].unique():
        flash("Invalid State", 'error')
        return redirect(url_for('state_analysis'))  # Redirect to the state_analysis page

    # Check if the year exists in the dataset for the given state
    if year not in df[df['State'] == state]['Year'].unique():
        flash(f"No data available for {state} in {year}", 'error')
        return redirect(url_for('state_analysis'))  # Redirect to the state_analysis page

    # Perform state analysis and generate plots
    pie_chart = plot_pie_chart(state, year)
    bar_chart = plot_bar_chart(state, year)

    return render_template('state_analysis.html', state=state, year=year, pie_chart=pie_chart, bar_chart=bar_chart)

@app.route('/state_analysis')
def state_analysis():
    return render_template('state_analysis.html')

@app.route('/tableau_visualization')
def tableau_visualization():
    # Replace 'path/to/tableau/dashboard' with the actual path to your Tableau dashboard file
    tableau_path = 'D:/final year project/Energy Analytics.twb'
    # Open Tableau dashboard using the default program associated with .twb files
    os.startfile(tableau_path)
    return render_template('tableau_visualization.html')

@app.route('/global_analysis')
def global_analysis():
    return render_template('global_analysis.html')

@app.route('/show_global_image')
def show_global_image():
    # Replace 'path/to/global/image' with the actual path to the global image
    global_image_path = 'D:/final year project/gui/static/global_prediction.png'
    return render_template('show_image.html', image_path=global_image_path)

@app.route('/show_india_image')
def show_india_image():
    # Replace 'path/to/india/image' with the actual path to the India image
    india_image_path = 'D:/final year project/gui/static/india_prediction.jpg'
    return render_template('show_image.html', image_path=india_image_path)


if __name__ == '__main__':
    app.run(debug=True)

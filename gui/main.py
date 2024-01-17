import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Make sure to install Pillow using: pip install Pillow

# Function for the first button - State Analysis and Prediction
def state_analysis():
    messagebox.showinfo("State Analysis", "Perform state analysis and prediction here")

# Function for the second button - Tableau Visualization
def tableau_visualization():
    # Replace 'path/to/tableau/dashboard' with the actual path to your Tableau dashboard file
    # You can use Tableau Reader or Tableau Public to publish your dashboard and get the file path
    tableau_path = 'path/to/tableau/dashboard'
    # Open Tableau dashboard using default program associated with .twb files
    import os
    os.system(f'start {tableau_path}')

# Function for the third button - Global Analysis and Prediction
def global_analysis():
    global_analysis_window = tk.Toplevel(root)
    global_analysis_window.title("Global Analysis and Prediction")

    # Function for the global button
    def show_global_image():
        global_image_path = 'D:/final year project/gui/static/global_prediction.png'  # Replace with the actual path to the global image
        show_image(global_image_path)

    # Function for the India button
    def show_india_image():
        india_image_path = 'static/india_prediction.jpg'  # Replace with the actual path to the India image
        show_image(india_image_path)

    global_button = tk.Button(global_analysis_window, text="Global", command=show_global_image)
    global_button.pack()

    india_button = tk.Button(global_analysis_window, text="India", command=show_india_image)
    india_button.pack()

# Function to show an image in a new window
def show_image(image_path):
    image_window = tk.Toplevel(root)
    image_window.title("Image Viewer")

    img = Image.open(image_path)
    # Resize the image to fit within the window
    img = img.resize((1000, 700), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    label = tk.Label(image_window, image=img)
    label.image = img
    label.pack()

# Main Tkinter window
root = tk.Tk()
root.title("Main Window")

# Button 1 - State Analysis and Prediction
button1 = tk.Button(root, text="State Analysis and Prediction", command=state_analysis)
button1.pack()

# Button 2 - Tableau Visualization
button2 = tk.Button(root, text="Tableau Visualization", command=tableau_visualization)
button2.pack()

# Button 3 - Global Analysis and Prediction
button3 = tk.Button(root, text="Global Analysis and Prediction", command=global_analysis)
button3.pack()

# Start the Tkinter event loop
root.mainloop()

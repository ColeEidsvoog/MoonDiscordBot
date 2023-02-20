# Importing required modules
from flask import Flask
from threading import Thread

# Creating a new Flask application object
app = Flask('')

# Defining the route for the homepage
@app.route('/')
def home():
    return "Bot is awake!"

# Function to run the Flask app on the specified host and port
def run():
  app.run(host='0.0.0.0',port=8080)

# Function to keep the app awake by running it in a separate thread
def keep_alive():
  # Creating a new thread and assigning the 'run' function to it
  t = Thread(target=run)
  # Starting the thread
  t.start()
# app.py
import os
import pandas as pd
import flask
import webview
import json

# --- Constants ---
CSV_FILE = "actions.csv"
COLUMNS = ["id", "action", "duration_h", "duration_m", "objective", "outcome", "rating"]

# --- Flask App Setup ---
app = flask.Flask(__name__, static_folder='./templates')
# We don't need to cache the UI file during development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 

# --- Backend API Routes ---

# This route serves our main HTML user interface
@app.route('/')
def home():
    return flask.render_template('index.html')

# This is our API for getting and saving the data
@app.route('/api/actions', methods=['GET', 'POST'])
def api_actions():
    # When the frontend asks for data (GET)
    if flask.request.method == 'GET':
        if os.path.exists(CSV_FILE):
            df = pd.read_csv(CSV_FILE)
            # Convert dataframe to a list of dictionaries (JSON)
            return df.to_json(orient='records')
        else:
            # If no file exists, return an empty list
            return json.dumps([])

    # When the frontend sends data to be saved (POST)
    elif flask.request.method == 'POST':
        # Get the JSON data sent from the frontend
        actions_data = flask.request.get_json()
        
        # Convert it to a pandas DataFrame
        df = pd.DataFrame(actions_data, columns=COLUMNS)
        
        # Save it to our CSV file
        df.to_csv(CSV_FILE, index=False)
        
        # Return a success message
        return {"status": "success"}

    return {"status": "error", "message": "Invalid method"}


if __name__ == '__main__':
    # Create a webview window
    window = webview.create_window('Daily Action Tracker', app, width=1200, height=800)
    webview.start()
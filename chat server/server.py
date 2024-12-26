import socket
import json
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Load messages from JSON file
MESSAGES_FILE = 'messages.json'

def load_messages():
    try:
        with open(MESSAGES_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_messages_async(messages):
    """
    Save messages to a file asynchronously using threading.
    """
    def save():
        with open(MESSAGES_FILE, 'w') as file:
            json.dump(messages, file)
    
    save_thread = threading.Thread(target=save)
    save_thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    # Send the previous messages to the client
    messages = load_messages()
    emit('load_previous_messages', messages)

@socketio.on('send_message')
def handle_message(data):
    # Get the message data (name, message, type)
    name = data.get('name')
    message = data.get('message')
    message_type = data.get('type')

    # Store the message in the messages list
    messages = load_messages()
    message_data = {'name': name, 'message': message, 'type': message_type}
    messages.append(message_data)
    
    # Save the messages to the file asynchronously
    save_messages_async(messages)

    # Emit the message to all connected clients
    emit('receive_message', message_data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

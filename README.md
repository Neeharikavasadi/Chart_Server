# Chart_Server

## Description
Chart_Server is a simple chat application built using Flask and Socket.IO that allows users to communicate in real-time. It features an elegant user interface where users can send text messages and images, and the messages are stored in a JSON file.

## 🌟Features and Functionality
- Real-time messaging using WebSockets.
- Ability to send and receive text messages.
- Support for sending images.
- Previous messages are loaded when a user connects.
- Responsive and modern UI.

## 🛠 Technology Stack
- **Backend**: Flask
- **WebSockets**: Flask-SocketIO
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: JSON file

## 📋Prerequisites
To run this project, you need to have:
- Python 3.6 or higher
- pip (Python package installer)

## 🚀 Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Neeharikavasadi/Chart_Server.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Chart_Server/chat\ server
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required packages:
   ```bash
   pip install flask flask-socketio
   ```

## ⚙️Usage Guide
1. To start the server, run the following command in the terminal:
   ```bash
   python server.py
   ```
2. Open your web browser and go to `http://localhost:5000` to access the chat application.
3. Enter your name and start chatting!

## 📡API Documentation
- **POST /send_message**
  - Sends a message to all connected clients.
  - Payload Structure:
    ```json
    {
      "name": "User Name",
      "message": "Your message",
      "type": "text" // or "image"
    }
    ```

- **GET /**
  - Serves the main chat interface.

## 🤝 Contributing Guidelines
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.


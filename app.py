from flask import Flask, request, jsonify
from flask_cors import CORS # This allows the frontend to talk to the backend

app = Flask(__name__)
CORS(app) 

# This is our temporary "Memory" (The Database)
messages = ["Welcome to the class!"]

@app.route('/get-messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/send-message', methods=['POST'])
def add_message():
    data = request.json
    messages.append(data['text'])
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
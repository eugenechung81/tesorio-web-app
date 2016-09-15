import sys
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


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

from flask import Flask, jsonify
from flask_cors import CORS
from hms import create_app


print(create_app)

app = create_app()
# configuration
DEBUG = True

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

if __name__ == '__main__':
    app.run()
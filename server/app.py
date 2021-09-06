from flask_cors import CORS

from hms import create_app


app = create_app()

# configuration
DEBUG = True

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
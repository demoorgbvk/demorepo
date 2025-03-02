from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the app on localhost and port 5000
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.before_first_request
def create_tables():
    print("Creating tables...")

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

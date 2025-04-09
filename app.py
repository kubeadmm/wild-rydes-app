from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Company: Wild Rydes | Developer: Rahul Dhaka p | ID: 100953252"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/dashboard')
def dashboard():
    return 'This the dashboard!'

@app.route('/login')
def login():
    return 'this is the login page '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
#run this folder using command: sudo python3 app.py to run file#

#sudo nohup python3 app.py > log.txt 2>&1 &
#ran this to have it be rerun in the backround
from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect('success')

@app.route('/success')
def success():
    return 'this is a new change test'

if __name__ == '__main__':
    app.run(host="localhost", port=80, debug=True)

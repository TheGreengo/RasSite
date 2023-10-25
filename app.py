from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

todos = []

@app.route("/")
def index():
    return render_template('main.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    return render_template('main.html', todos=todos)

@app.route('/remove', methods=['DELETE'])
def remove():
    return render_template('main.html', todos=todos)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
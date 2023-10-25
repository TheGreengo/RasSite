from flask import Flask, redirect, url_for, request, render_template
import numpy as np

app = Flask(__name__)

todos = []

@app.route("/")
def index():
    return render_template('main.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    desc = request.form.get("desc")
    id = np.random.randint(2000000000)
    todos.append({ "desc": desc, "id": id})
    print(todos)
    return render_template('main.html', todos=todos)

@app.route('/remove/<id>', methods=['POST'])
def remove():
    return render_template('main.html', todos=todos)

@app.route('/clear', methods=['POST'])
def clear():
    todos.clear()
    return render_template('main.html', todos=todos)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data
todo_item = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/todo")
def get_todo():
    return jsonify(todo_item)

if __name__ == "__main__":
    app.run(debug=True)

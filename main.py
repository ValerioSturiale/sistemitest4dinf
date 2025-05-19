from flask import Flask, render_template

app = Flask(__name__, template_folder="src")

# Lista di post da mostrare nel template
posts = [
    {"title": "Post 1", "content": "Questo è il contenuto del post 1"},
    {"title": "Post 2", "content": "Questo è il contenuto del post 2"},
    {"title": "Post 3", "content": "Questo è il contenuto del post 3"},
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Puoi cambiare la porta se necessario


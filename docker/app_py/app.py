import os
import sqlite3
from contextlib import closing
from pathlib import Path

from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)
app.config["DB_PATH"] = os.environ.get("DB_PATH", "app.db")

PAGE = """
<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Cadastro de itens</title>
    <style>
        * { box-sizing: border-box; }
        body { margin: 0; color: #202923; background: #f5f7f6;
               font-family: "Trebuchet MS", sans-serif; }
        main { max-width: 640px; margin: 48px auto; padding: 0 24px; }
        h1 { font-size: 28px; }
        h2 { margin-top: 40px; font-size: 20px; }
        label { display: block; margin-bottom: 8px; }
        input { width: 100%; padding: 12px; border: 1px solid #89988e;
                border-radius: 4px; font: inherit; }
        button { margin-top: 12px; padding: 12px 20px; border: 0;
                 border-radius: 4px; background: #17623b; color: white;
                 font: inherit; cursor: pointer; }
        button:hover { background: #104a2c; }
        li { padding: 12px 0; border-bottom: 1px solid #d4ded7;
             overflow-wrap: anywhere; }
        ul { list-style: none; padding: 0; }
        .error { color: #a12727; }
    </style>
</head>
<body>
    <main>
        <h1>Cadastro de itens</h1>
        <form method="post" action="{{ url_for('index') }}">
            <label for="name">Nome do item</label>
            <input id="name" name="name" required value="{{ name }}">
            <button type="submit">Cadastrar item</button>
        </form>
        {% if error %}<p class="error" role="alert">{{ error }}</p>{% endif %}
        <h2>Itens cadastrados</h2>
        <ul>
            {% for item in items %}
                <li>{{ item[0] }}</li>
            {% else %}
                <li>Nenhum item cadastrado.</li>
            {% endfor %}
        </ul>
    </main>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
	db_path = Path(app.config["DB_PATH"])
	db_path.parent.mkdir(parents=True, exist_ok=True)
	error = None
	name = ""
	with closing(sqlite3.connect(db_path)) as connection:
		with connection:
			connection.execute(
				"CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT NOT NULL)"
			)
			if request.method == "POST":
				name = request.form.get("name", "").strip()
				if name:
					connection.execute("INSERT INTO items (name) VALUES (?)", (name,))
				else:
					error = "Informe o nome do item."

		if request.method == "POST" and error is None:
			return redirect(url_for("index"))
		items = connection.execute("SELECT name FROM items ORDER BY id DESC").fetchall()

	return render_template_string(PAGE, items=items, error=error, name=name), 400 if error else 200


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=3000)

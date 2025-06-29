from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)


def load_quotes():
    with open("quotes_base.json", "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    all_quotes = load_quotes()
    quote = random.choice(all_quotes)
    return render_template("index.html", quote=quote)


@app.route("/api/random")
def api_random():
    all_quotes = load_quotes()
    quote = random.choice(all_quotes)
    return jsonify(quote)


if __name__ == "__main__":
    app.run(debug=True)


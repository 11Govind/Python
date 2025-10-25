from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

heads_count = 0
tails_count = 0

@app.route("/")
def index():
    return render_template("index.html", heads=heads_count, tails=tails_count)

@app.route("/flip")
def flip_coin():
    global heads_count, tails_count
    result = random.choice(["Heads", "Tails"])
    if result == "Heads":
        heads_count += 1
    else:
        tails_count += 1
    return jsonify({"result": result, "heads": heads_count, "tails": tails_count})

if __name__ == "__main__":
    app.run(debug=True)

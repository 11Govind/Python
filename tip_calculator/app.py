from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def tip_calculator():
    if request.method == "POST":
        bill = float(request.form["bill"])
        tip = int(request.form["tip"])
        people = int(request.form["people"])
        final_bill = round((bill + (bill * tip / 100)) / people, 2)
        return render_template("index.html", result=final_bill)
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)

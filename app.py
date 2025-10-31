from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def PrimerPWBI():
    return render_template("PrimerPWBI.html")

if __name__ == "__main__":
    app.run(debug=True)
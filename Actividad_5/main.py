from flask import Flask, render_template

app = Flask(__name__)

# Landing page
@app.route("/")
def landing():
    return render_template("index.html")

# Mapa interactivo
@app.route("/map")
def mapa():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)

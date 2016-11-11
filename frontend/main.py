from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    to_search = request.form["input"]
    s_date, e_date = request.form["s_date"], request.form["e_date"]
    if s_date:
        s_date = s_date.split("-")
        s_date = "{0}-{1}-{2}".format(s_date[2], s_date[1], s_date[0])
    if e_date:
        e_date = e_date.split("-")
        e_date = "{0}-{1}-{2}".format(e_date[2], e_date[1], e_date[0])

# Aqui debe ir la consulta de mongo. Hay que guardar los articulos en
# articles. Flask dsp hará magia.

    articles = []
    for file in os.listdir("../sources/fu"):
        with open("{0}/{1}".format("../sources/fu", file)) as f:
            articles.append(json.load(f))

#---------------------------------------------------------------------

    return render_template("search.html", search=to_search,
                           articles=articles)

if __name__ == '__main__':
    app.run("127.0.0.2")

#Alessandro Cartegni
#SoftDev1 pd7
#HW13 -- A RESTful Journey Skyward
#2017-11-09

from flask import Flask, render_template
import json
import urllib2


app = Flask(__name__)

@app.route("/")
def home():
    #resp = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=ElpxYSG5sKBZ4PjXbK6EROAt2nnr5QtKwqqDt7e7')
    resp = urllib2.urlopen('http://www.omdbapi.com/?i=tt3896198&apikey=68f529d5')
    j = resp.read()
    d = json.loads(j)
    return render_template('home.html', title = d["Title"], director = d["Director"], actors = d["Actors"], plot = d["Plot"], poster = d["Poster"])



if __name__ == "__main__":
    app.debug = True
    app.run()

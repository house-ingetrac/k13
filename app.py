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
    uResp = urllib2.urlopen(https://api.nasa.gov/planetary/apod?api_key=ElpxYSG5sKBZ4PjXbK6EROAt2nnr5QtKwqqDt7e7)
    d = json.loads(uResp.read())
    return render_template('home.html', title = d["title"])



if __name__ == "__main__":
    app.debug = True
    app.run()

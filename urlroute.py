## flask app routing

from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET"])

def welcome():
    return "<h1>welcome to flask app Tanvir</h1>"


@app.route("/index",methods=["GET"])
def index():
    return "welcome to index page"

@app.route("/about",methods=["GET"])
def about():
    return "welcome to my about page brother"

@app.route("/success/<int:score>")
def success (score):
    return "the person has passed and the score is "+str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "the person has failed and the score is "+str(score)

@app.route('/form',methods=["POST","GET"])
def form():
    if request.method=="GET":
        return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True)
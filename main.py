from flask import Flask, render_template

app=Flask(__name__,
          template_folder="templates",
          static_folder="static")


@app.route("/")
@app.route("/index.html")
@app.route("/index")
def index():

    return render_template('index.html')


@app.route("/home")
@app.route("/home.html")
def home():
    return render_template('home.html')


@app.route("/Fresh_start.html")
@app.route("/Fresh_start")
@app.route("/page1")
def page1():
    return render_template ('Fresh_start.html')





if __name__=="__main__":
    app.run(app.run(host="127.0.0.1", port=5000,debug=True))
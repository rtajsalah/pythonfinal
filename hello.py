from flask import Flask, render_template, request
app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/<name>")
def hello_someone(name):
          return render_template("hello.html", name=name.title())

@app.route("/about.html")
def about():
          return render_template("about.html")

@app.route("/contactus.html")
def contactus():
         return render_template("contactus.html")

app.run(debug=True)

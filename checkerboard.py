from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:num>')
def index1(num):
    return render_template("index1.html", num=num)

@app.route('/<int:num2>/<int:num1>')
def index2(num2,num1):
    return render_template("index2.html", num2=num2, num1=num1)

@app.route('/<int:num2>/<int:num1>/<color1>/<color2>')
def index3(num2,num1,color1,color2):
    return render_template("index3.html", num2=num2, num1=num1, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)
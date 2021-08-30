from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Render():
    return render_template("index.html")

@app.route('/html_tutorial_home.html')
def Render_index():
    return render_template("html_tutorial_home.html")
# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
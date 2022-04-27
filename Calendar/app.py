from flask import Flask, render_template

# app=Flask('Full Year Calendar')
app=Flask(__name__)

@app.route('/')
def home():
    # return render_template(index.html)
    return "Hello World!!"

@app.route('/cal')
def calendar():
    return render_template("calendar.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
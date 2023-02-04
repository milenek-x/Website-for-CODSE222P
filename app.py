from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/notes')
def notes():
	return render_template("notes.html")

@app.route('/videos')
def videos():
	return render_template("videos.html")

@app.route('/vid-ics')
def ics():
	return render_template("ics-videos.html")

@app.route('/vid-ecs1')
def ecs1():
	return render_template("ecs1-videos.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

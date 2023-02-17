from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/notes')
def notes():
	return render_template("notes.html")

@app.route('/notes-pf')
def notespf():
	return render_template("pf-notes.html")

@app.route('/notes-ecs1')
def notesecs1():
	return render_template("ecs1-notes.html")

@app.route('/notes-ics')
def notesics():
	return render_template("ics-notes.html")

@app.route('/multimedia')
def multimedia():
	return render_template("multimedia.html")

@app.route('/mm-ics')
def mmics():
	return render_template("ics-multimedia.html")

@app.route('/mm-pf')
def mmpf():
	return render_template("pf-multimedia.html")

@app.route('/mm-pf-vc')
def mmpfvc():
	return render_template("pf-virtual-classrooms.html")

@app.route('/mm-pf-other')
def mmpfother():
	return render_template("pf-other-multimedia.html")

@app.route('/mm-ecs1')
def mmecs1():
	return render_template("ecs1-multimedia.html")

@app.route('/mm-ecs1-vc')
def mmecs1mmvc():
	return render_template("ecs1-virtual-classrooms.html")

@app.route('/mm-ecs1-other')
def ecs1mmother():
	return render_template("ecs1-other-multimedia.html")

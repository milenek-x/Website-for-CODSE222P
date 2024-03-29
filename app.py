from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))

# Define routes
@app.route("/")
def index():
    # Render the home page template
    return render_template("index.html")

@app.route("/introduction-to-computer-science")
def introduction_to_computer_science():
    # Render the Introduction to Computer Science page template
    return render_template("introduction_to_computer_science.html")

@app.route("/programming-fundamentals")
def programming_fundamentals():
    # Render the Programming Fundamentals page template
    return render_template("programming_fundamentals.html")

@app.route("/mathematics-for-computing")
def mathematics_for_computing():
    # Render the Mathematics for Computing page template
    return render_template("mathematics_for_computing.html")

@app.route("/database-management-systems")
def database_management_systems():
    # Render the Database Management Systems page template
    return render_template("database_management_systems.html")

@app.route("/object-oriented-programming")
def object_oriented_programming():
    # Render the Object Oriented Programming page template
    return render_template("object_oriented_programming.html")

@app.route("/electronics-and-computer-architecture")
def electronics_and_computer_architecture():
    # Render the Electronics and Computer Architecture page template
    return render_template("electronics_and_computer_architecture.html")

@app.route("/gui-application-development")
def gui_application_development():
    # Render the GUI Application Development page template
    return render_template("gui_application_development.html")

@app.route("/software-engineering")
def software_engineering():
    # Render the GUI Application Development page template
    return render_template("software_engineering.html")

@app.route("/effective-communication-skills-1")
def effective_communication_skills_1():
    # Render the Effective Communication Skills-1 page template
    return render_template("effective_communication_skills_1.html")

# Add more routes for additional modules...

if __name__ == "__main__":
    # Start the development server
    app.run(debug=True)

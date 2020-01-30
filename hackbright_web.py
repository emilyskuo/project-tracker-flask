"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student-add")
def student_add():
    """Display form to add a student"""


    return render_template('student_add.html')


@app.route("/student-add", methods=['POST'])
def added_student():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template('added_student.html', first_name=first_name,
                                                 last_name=last_name,
                                                 github=github)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    grades = hackbright.get_grades_by_github(github)


    html = render_template("students_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades=grades)
    return html

    #http://127.0.0.1:5000/student?github=jhacks

@app.route("/project")
def get_project():
    """Show information about a student."""

    title = request.args.get('title')

    title, description, max_grade = hackbright.get_project_by_title(title)

    html = render_template("project_info.html",
                           title=title,
                           description=description,
                           max_grade=max_grade)
    return html
    #http://127.0.0.1:5000/project?title=Markov






@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")

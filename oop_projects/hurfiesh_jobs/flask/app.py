from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/jobs')  # Jobs page
def jobs():
    return render_template('jobs.html')


@app.route('/professionals')  # Professionals page
def professionals():
    return render_template('professionals.html')


@app.route('/find_job')
def find_job():
    from oop_projects.hurfiesh_jobs.src.classes.job import Job
    return render_template('find_job.html')


@app.route('/find_professional', methods=['GET', 'POST'])
def find_professional():
    from oop_projects.hurfiesh_jobs.src.classes.professional import Professional
    name = None
    result = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()  # Get name from form and strip extra spaces
        if name:
            result = Professional.find_professional(name)
        else:
            result = "Please enter a name to search."  # Provide feedback if name is empty

    return render_template('find_professional.html', name=name, result=result)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

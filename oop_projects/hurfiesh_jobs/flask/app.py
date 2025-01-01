from flask import Flask, render_template, request
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/jobs')  # Jobs page
def jobs():
    from src.classes.jobs import Job
    return render_template('jobs.html', jobs=Job.show_jobs())


@app.route('/professionals')  # Professionals page
def professionals():
    from src.classes.professional import Professional
    return render_template('professionals.html', professionals=Professional.show_professionals())


@app.route('/find_job', methods=['GET', 'POST'])
def find_job():
    from src.classes.jobs import Job
    name = None
    result = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()  # Get name from form and strip extra spaces
        if name:
            result = Job.find_job(name)
        else:
            result = "Please enter a name to search."  # Provide feedback if name is empty
    return render_template('find_job.html', name=name, result=result)


@app.route('/find_professional', methods=['GET', 'POST'])
def find_professional():
    from src.classes.professional import Professional
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
    app.run(debug=True, port=5000, host='0.0.0.0')

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')  # Home page
def home():
    return render_template('home.html')


@app.route('/jobs')  # Jobs page
def jobs():
    return render_template('jobs.html')


@app.route('/professionals')  # Professionals page
def professionals():
    return render_template('professionals.html')


app.route('/find_job')


def find_job():
    return render_template('find_job.html')


@app.route('/find_professional')
def find_professional():
    return render_template('find_professional.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home_page():
   return render_template("home.html")


@app.route('/home')
def return_home():
   return render_template("home.html")


@app.route('/report')
def report_page():
   return render_template("report.html")


@app.route('/API')
def API_page():
   return render_template("API.html")

@app.route('/calculation', methods=['GET', 'POST'])
def calculate_score():
   return render_template('home.html')


if __name__ == '__main__':
   app.run()
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from MySQLdb import escape_string as thwart
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'amber'
app.config['MYSQL_DB'] = 'reviews'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/welcome')
def  welcome():
    return render_template('welcome.html')

@app.route('/social')
def social():
    return render_template('social.html')
@app.route('/corruption',methods=['GET', 'POST'])
def corruption():
    return render_template('corruption.html')
@app.route('/reservation')
def reservation():
    return render_template('reservation.html')
@app.route('/politics')
def politics():
    return render_template('politics.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')
@app.route('/internet')
def internet():
    return render_template('internet.html')
@app.route('/env')
def env():
    return render_template('env.html')
	
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)

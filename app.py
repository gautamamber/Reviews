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

@app.route('/social',methods=['GET', 'POST'])
def social():
    if request.method == 'POST':
        try:
            name = request.form['name']
            
         
            email = request.form['email']
            s1 = request.form['s1']
            
         
            s2 = request.form['s2']
            s3 = request.form['s3']
            
         
            s4 = request.form['s4']
            s5 = request.form['s5']
            
         
            s6 = request.form['s6']
            s7 = request.form['s7']
            
         
            s8 = request.form['s8']
            
            cur = mysql.connection.cursor()
            x = cur.execute("SELECT * FROM social WHERE email = (%s)",(thwart(email),))


            if cur.fetchone() is not None:
                flash('Sorry, Email already registered', 'success')

                return redirect(url_for('social'))
            else:
                cur.execute("INSERT INTO social(name,email,s1,s2,s3,s4,s5,s6,s7,s8) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,s1,s2,s3,s4,s5,s6,s7,s8))        
                mysql.connection.commit()

            # Close connection
                cur.close()
            

                return redirect(url_for('home'))
        except Exception as e:
            return(str(e))
        
            return redirect(url_for('home'))
    return render_template('social.html')
@app.route('/corruption',methods=['GET', 'POST'])
def corruption():
    if request.method == 'POST':
        try:
            name = request.form['name']
            
         
            email = request.form['email']
            c1 = request.form['c1']
            
         
            c2 = request.form['c2']
            c3 = request.form['c3']
            
         
            c4 = request.form['c4']
            c5 = request.form['c5']
            
         
            c6 = request.form['c6']
            c7 = request.form['c7']
            
         
            c8 = request.form['c8']
            
            cur = mysql.connection.cursor()
            x = cur.execute("SELECT * FROM curroption WHERE email = (%s)",(thwart(email),))


            if cur.fetchone() is not None:
                flash('Sorry, Email already registered', 'success')

                return redirect(url_for('corruption'))
            else:
                cur.execute("INSERT INTO curroption(name,email,c1,c2,c3,c4,c5,c6,c7,c8) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,c1,c2,c3,c4,c5,c6,c7,c8))        
                mysql.connection.commit()

            # Close connection
                cur.close()
            

                return redirect(url_for('home'))
        except Exception as e:
            return(str(e))
        
            return redirect(url_for('home'))
    return render_template('corruption.html')

@app.route('/reservation', methods=['GET','POST'])
def reservation():
    if request.method == 'POST':
        try:
            name = request.form['name']
            
         
            email = request.form['email']
            r1 = request.form['r1']
            
         
            r2 = request.form['r2']
            r3 = request.form['r3']
            
         
            r4 = request.form['r4']
            r5 = request.form['r5']
            
         
            r6 = request.form['r6']
            r7 = request.form['r7']
            
         
            r8 = request.form['r8']
            
            cur = mysql.connection.cursor()
            x = cur.execute("SELECT * FROM reservation WHERE email = (%s)",(thwart(email),))


            if cur.fetchone() is not None:
                flash('Sorry, Email already registered', 'success')

                return redirect(url_for('reservation'))
            else:
                cur.execute("INSERT INTO reservation(name,email,r1,r2,r3,r4,r5,r6,r7,r8) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,r1,r2,r3,r4,r5,r6,r7,r8))        
                mysql.connection.commit()

            # Close connection
                cur.close()
            

                return redirect(url_for('home'))
        except Exception as e:
            return(str(e))
        
            return redirect(url_for('home'))
    return render_template('reservation.html')
    
@app.route('/politics',methods=['GET','POST'])
def politics():
    if request.method == 'POST':
        try:
            name = request.form['name']
            
         
            email = request.form['email']
            p1 = request.form['p1']
            
         
            p2 = request.form['p2']
            p3 = request.form['p3']
            
         
            p4 = request.form['p4']
            p5 = request.form['p5']
            
         
            p6 = request.form['p6']
            p7 = request.form['p7']
            
         
            p8 = request.form['p8']
            
            cur = mysql.connection.cursor()
            x = cur.execute("SELECT * FROM politics WHERE email = (%s)",(thwart(email),))


            if cur.fetchone() is not None:
                flash('Sorry, Email already registered', 'success')

                return redirect(url_for('politics'))
            else:
                cur.execute("INSERT INTO politics(name,email,p1,p2,p3,p4,p5,p6,p7,p8) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,p1,p2,p3,p4,p5,p6,p7,p8))        
                mysql.connection.commit()

            # Close connection
                cur.close()
            

                return redirect(url_for('home'))
        except Exception as e:
            return(str(e))
        
            return redirect(url_for('home'))
    return render_template('politics.html')

@app.route('/education',methods=['GET','POST'])
def education():
    if request.method == 'POST':
        try:
            name = request.form['name']
            
         
            email = request.form['email']
            d1 = request.form['d1']
            
         
            d2 = request.form['d2']
            d3 = request.form['d3']
            
         
            d4 = request.form['d4']
            d5 = request.form['d5']
            
         
            d6 = request.form['d6']
            d7 = request.form['d7']
            
         
            d8 = request.form['d8']
            
            cur = mysql.connection.cursor()
            x = cur.execute("SELECT * FROM education WHERE email = (%s)",(thwart(email),))


            if cur.fetchone() is not None:
                flash('Sorry, Email already registered', 'success')

                return redirect(url_for('education'))
            else:
                cur.execute("INSERT INTO education(name,email,d1,d2,d3,d4,d5,d6,d7,d8) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,d1,d2,d3,d4,d5,d6,d7,d8))        
                mysql.connection.commit()

            # Close connection
                cur.close()
            

                return redirect(url_for('home'))
        except Exception as e:
            return(str(e))
        
            return redirect(url_for('home'))
    return render_template('education.html')
    
    

@app.route('/movies',methods=['GET','POST'])
def movies():
    if request.method == 'POST':
        try:
            name = request.form['name']
            
         
            email = request.form['email']
            m1 = request.form['m1']
            
         
            m2 = request.form['m2']
            m3 = request.form['m3']
            
         
            m4 = request.form['m4']
            m5 = request.form['m5']
            
         
            m6 = request.form['m6']
            m7 = request.form['m7']
            
         
            m8 = request.form['m8']
            
            cur = mysql.connection.cursor()
            x = cur.execute("SELECT * FROM movies WHERE email = (%s)",(thwart(email),))


            if cur.fetchone() is not None:
                flash('Sorry, Email already registered', 'success')

                return redirect(url_for('movies'))
            else:
                cur.execute("INSERT INTO movies(name,email,m1,m2,m3,m4,m5,m6,m7,m8) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,m1,m2,m3,m4,m5,m6,m7,m8))        
                mysql.connection.commit()

            # Close connection
                cur.close()
            

                return redirect(url_for('home'))
        except Exception as e:
            return(str(e))
        
            return redirect(url_for('home'))
    return render_template('movies.html')
@app.route('/internet',methods=['GET','POST'])
def internet():
    if request.method == 'POST':
        try:
            name = request.form['name']
            
         
            email = request.form['email']
            i1 = request.form['i1']
            
         
            i2 = request.form['i2']
            i3 = request.form['i3']
            
         
            i4 = request.form['i4']
            i5 = request.form['i5']
            
         
            i6 = request.form['i6']
            i7 = request.form['i7']
            
         
            i8 = request.form['i8']
            
            cur = mysql.connection.cursor()
            x = cur.execute("SELECT * FROM internet WHERE email = (%s)",(thwart(email),))


            if cur.fetchone() is not None:
                flash('Sorry, Email already registered', 'success')

                return redirect(url_for('internet'))
            else:
                cur.execute("INSERT INTO internet(name,email,i1,i2,i3,i4,i5,i6,i7,i8) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,i1,i2,i3,i4,i5,i6,i7,i8))        
                mysql.connection.commit()

            # Close connection
                cur.close()
            

                return redirect(url_for('home'))
        except Exception as e:
            return(str(e))
        
            return redirect(url_for('home'))
    return render_template('internet.html')
@app.route('/env',methods=['GET','POST'])
def env():
    if request.method == 'POST':
        try:
            name = request.form['name']
            
         
            email = request.form['email']
            e1 = request.form['e1']
            
         
            e2 = request.form['e2']
            e3 = request.form['e3']
            
         
            e4 = request.form['e4']
            e5 = request.form['e5']
            
         
            e6 = request.form['e6']
            e7 = request.form['e7']
            
         
            e8 = request.form['e8']
            
            cur = mysql.connection.cursor()
            x = cur.execute("SELECT * FROM env WHERE email = (%s)",(thwart(email),))


            if cur.fetchone() is not None:
                flash('Sorry, Email already registered', 'success')

                return redirect(url_for('env'))
            else:
                cur.execute("INSERT INTO env(name,email,e1,e2,e3,e4,e5,e6,e7,e8) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,e1,e2,e3,e4,e5,e6,e7,e8))        
                mysql.connection.commit()

            # Close connection
                cur.close()
            

                return redirect(url_for('home'))
        except Exception as e:
            return(str(e))
        
            return redirect(url_for('home'))
    return render_template('env.html')
    
	
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)

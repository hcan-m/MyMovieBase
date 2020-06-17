from flask import Flask, render_template, request, redirect, url_for, session
import re
import sqlite3 as sql
from sqlite3 import connect
import os.path

app = Flask(__name__)

app.secret_key = '123'

BASE_DIR = os.path.dirname(os.path.abspath("C:\\Users\\hcanm\\Desktop\\MyMovieBase\\MyMovieBase_db.db"))
db_path = os.path.join(BASE_DIR, "MyMovieBase_db.db")
conn = sql.connect(db_path)
cursor = conn.cursor()

@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE username = ? AND password = ?", [username, password])
        account = cursor.fetchone()
        conn.commit()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)


@app.route('/login/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/login/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = ?', [username])
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, ?, ?, ?)', [username, password, email])
            conn.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)



@app.route('/login/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))


@app.route('/login/profile')
def profile():
    if 'loggedin' in session:
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE id = ?', [session['id']])
        account = cursor.fetchone()
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT moviesid,prefer FROM movies_users WHERE usersid = ?', [session['id']])
        item_lists = cursor.fetchall()
        watch_count = 0
        watched_count = 0
        for i in item_lists:
            watchlist = i[1]
            if watchlist == 1:
                watch_count += 1
            elif watchlist == 2:
                watched_count += 1
        return render_template('profile.html', account=account, watch_count=watch_count, watched_count=watched_count)
    return redirect(url_for('login'))


@app.route('/login/result')
def result():
    if 'loggedin' in session:
        if request.method == 'GET' and 'search_value' in request.args:
            search1 = request.args['search_value']
            search = '%' + search1 + '%'
            by_select = request.args['by_select']
            if by_select == "name":
                conn = sql.connect(db_path)
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM movie_detailed WHERE name like ?', [search])
                result1 = cursor.fetchall()
                return render_template('result.html', result=result1)
            if by_select == "director":
                conn = sql.connect(db_path)
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM movie_detailed WHERE director like ?', [search])
                result1 = cursor.fetchall()
                return render_template('result.html', result=result1)
            if by_select == "actors":
                conn = sql.connect(db_path)
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM movie_detailed WHERE actors like ?', [search])
                result1 = cursor.fetchall()
                return render_template('result.html', result=result1)
            if by_select == "genres":
                conn = sql.connect(db_path)
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM movie_detailed WHERE genres like ?', [search])
                result1 = cursor.fetchall()
                return render_template('result.html', result=result1)
    return redirect(url_for('login'))

@app.route('/create')
def create():
    if 'loggedin' in session:
        if request.method == 'GET':
            counter_added_movies = 0
            counter_existing_movies = 0
            movie1 = request.args
            movie = movie1.getlist("ids")
            pref = request.args["action"]
            conn = sql.connect(db_path)
            cursor = conn.cursor()
            for i in movie:
                cursor.execute('SELECT * FROM movies_users WHERE usersid = ? AND moviesid = ?', [session["id"], i])
                check = cursor.fetchall()
                if len(check) == 0:
                    cursor.execute('INSERT INTO movies_users (`usersid`, `moviesid`, `prefer`) VALUES (?, ?, ?)',
                                   [session["id"], i, pref])
                    counter_added_movies += 1
                else:
                    counter_existing_movies += 1
            conn.commit()
            if counter_existing_movies == 0:
                if counter_added_movies == 1:
                    errormsg = "%d movie successfully added to the list." % (counter_added_movies)
                else:
                    errormsg = "%d movies successfully added to the list." % (counter_added_movies)
            elif counter_added_movies == 0:
                if counter_existing_movies == 1:
                    errormsg = "%d movie already exist in your list." % (counter_existing_movies)
                else:
                    errormsg = "%d movies already exist in your list." % (counter_existing_movies)
            elif counter_added_movies == 1 and counter_existing_movies > 1:
                errormsg = "%d movie successfully added to the list. %d movies already exist in your list." % (counter_added_movies, counter_existing_movies)
            elif counter_added_movies > 1 and counter_existing_movies == 1:
                errormsg = "%d movies successfully added to the list. %d movie already exist in your list." % (counter_added_movies, counter_existing_movies)
            elif counter_added_movies == 1 and counter_existing_movies == 1:
                errormsg = "%d movie successfully added to the list. %d movie already exist in your list." % (counter_added_movies, counter_existing_movies)
            else:
                errormsg = "%d movies successfully added to the list. %d movies already exist in your list." % (counter_added_movies, counter_existing_movies)
            return render_template('home.html', errormessage=errormsg)
    return redirect(url_for('login'))


@app.route('/login/mylists')
def mylists():
    if 'loggedin' in session:
        if request.method == "GET":
            pref = request.args.get("action", default=1, type=int)
            conn = sql.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(
                'SELECT movie_id,name,director,duration,year,actors,genres,imdb_score,imdb_link FROM movie_detailed INNER JOIN movies_users '
                'ON movie_detailed.id=movies_users.moviesid WHERE usersid = ? and prefer = ?',
                [session["id"], pref])
            mylist = cursor.fetchall()
            return render_template('mylists.html', mylist=mylist, action=pref)
    return redirect(url_for('login'))
#action=1 watch list
#action=2 watched list

@app.route('/remove')
def remove():
    if 'loggedin' in session:
        if request.method == "GET":
            remid = request.args.getlist("ids")
            act = request.args["action"]
            for i in remid:
                conn = sql.connect(db_path)
                cursor = conn.cursor()
                cursor.execute('DELETE FROM movies_users WHERE usersid = ? and moviesid = ?', [session["id"], i])
            conn.commit()
            return redirect('/login/mylists?action=' + act)
    return redirect(url_for('login'))

@app.route('/towatched')
def towatched():
    if 'loggedin' in session:
        if request.method == "GET":
            mids = request.args.getlist("ids")
            conn = sql.connect(db_path)
            cursor = conn.cursor()
            for i in mids:
                cursor.execute('UPDATE movies_users SET prefer = 2 WHERE usersid = ? and moviesid = ?;', [session["id"], i])
            conn.commit()
            return redirect('/login/mylists')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

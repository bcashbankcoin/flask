from flask import Flask, render_template, redirect, url_for, request, flash, session, current_app
from blog import Bootstrap
from .models import User
from blog import app, mysql, mail , Message,bcrypt, db 
from itsdangerous import URLSafeSerializer, SignatureExpired
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
import secrets
import os
import re
import urllib.parse
import uuid
import math
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def save_images(photo):
     hash_photo = secrets.token_urlsafe(10)
     _, file_extention = os.path.splitext(photo.filename)
     photo_name = hash_photo + file_extention
     file_path = os.path.join(current_app.root_path, 'static/images', photo_name)
     photo.save(file_path)
     return photo_name




"""
@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        find = request.form.get('search')
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM blog WHERE title = %s ', (find))
        blog = cursor.fetchall()
"""


@app.route('/', defaults={'page':1})
@app.route('/page/<int:page>')
def home(page):
    limit = 3
    offset = page*limit - limit
    
    my_cursor =  mysql.connection.cursor() # my_connect is the connection 
    my_cursor.execute("SELECT * FROM  blog Where blog_id")
    total_row = my_cursor.rowcount
    total_page = math.ceil(total_row / limit )
    print('TOTAL', total_page)
    print('TOTAL Row', total_row)
    

    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM blog ORDER BY blog_id DESC LIMIT %s OFFSET %s ",(limit,offset))
    if resultValue > 0:
        blogs = cur.fetchall()
        cur.close()
        return render_template('index.html', blogs=blogs, page=total_page )
    return render_template('index.html' )    

'''
 
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search = request.form['search']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM blog WHERE title=%s",[search])
        results = cur.fetchall()
        cur.close()
        print(results)
        return render_template('search.html', results=results)
      
    return render_template('index.html')
'''


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search = request.form['search']
        cur = mysql.connection.cursor()
        query_string = "SELECT * FROM blog WHERE title LIKE %s ORDER BY blog_id ASC"
        cur.execute(query_string, ('%' + search + '%',))
        results = cur.fetchall()
        cur.close()
        flash('Showing result for: ' + search, 'success')
        print(results)
        return render_template('search.html', results=results)
      
    return render_template('index.html')  

@app.route('/dashboard')
def dashboard():
    if 'login' not in session:
        return redirect('/')
    first_name = session['firstname']   
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM user WHERE first_name =%s ",[first_name])
    if result_value > 0:
        user = cur.fetchone()    
        return render_template('about.html', user=user)


@app.route('/contact', methods=['GET', 'POST'] )
def contact():
    author = session['firstname'] + ' ' + session['lastname']
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        msg = request.form.get('msg')
        author = session['firstname'] + ' ' + session['lastname']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contact(name,email,subject,msg,author)" "VALUES(%s,%s,%s,%s,%s)",(name,email,subject,msg,author))
        mysql.connection.commit()
        cur.close()
        flash(' Your Message has been sent successfully','success')
        return redirect('/contactinfo')
    return render_template('contact.html')    

@app.route('/blogs/<int:id>', methods=['GET', 'POST'])
def blogs(id):  
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM blog WHERE blog_id = %s",[id])
    blog = cur.fetchone()
    blog_id = blog['blog_id'] 

    views = blog['views']
    newviews = views +1

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM comment  WHERE blog_id = %s ORDER BY id DESC ", [blog_id])
    comment = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute("UPDATE blog SET views = %s where blog_id = %s",(newviews, id))
    mysql.connection.commit()
    cur.close()

    """
    cur = mysql.connection.cursor()
    cur.execute("UPDATE blog SET comments = %s where blog_id = %s",( id))
    mysql.connection.commit()
    cur.close()

    """

    if request.method == 'POST':
        author = session['firstname'] + ' ' + session['lastname']
        comment = request.form['comment'] 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO comment ( blog_id, comment, author) VALUES (  %s, %s, %s)", ( blog_id, comment, author))
        mysql.connection.commit()
        
        blogcom = blog['comments']
        comment = blogcom + 1
        cur = mysql.connection.cursor()
        cur.execute("UPDATE blog SET comments = %s where blog_id = %s",(comment, id))
        mysql.connection.commit()
        cur.close()
        
        flash('Your comment successfull','success')
        return redirect(request.url)   
    return render_template('blogs.html', blog=blog, comment=comment)

       

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'login' in session:
        return redirect('/')
    if request.method == 'POST':    
        firstname = request.form.get('first_name')
        lastname = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirm_password')
        if password != confirmpassword:
            flash('Passwords do not match! Try again.', 'danger')
            return render_template('register.html')
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE email=%s',[email])
        user = cursor.fetchone()
        if user: 
            flash('Email already registerd !!!!','danger')   
        else:
            cur = mysql.connection.cursor()
            user = cur.execute("INSERT INTO user(first_name, last_name, username, email, password) "\
        "VALUES(%s,%s,%s,%s,%s)",(firstname, lastname, \
        username, email, bcrypt.generate_password_hash(password ))) #, 'pbkdf2:sha256' , 8
        
            mysql.connection.commit()
            cur.close()
            flash('Registration successful! Please login.', 'success')
            return redirect('/login')
    return render_template('register.html', title='Resister Page') 



@app.route('/login',methods=['GET','POST'])
def login():
    if 'login' in session:
        return redirect('/')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM user WHERE username =%s",[username])
        if resultValue >0:
            data = cur.fetchone()
            password1 = data['password']
            print((password))
           # print(bcrypt.check_password_hash(password1, password))
            #print(bcrypt.check_password_hash(password1, 'password'))
		   
            if (bcrypt.check_password_hash(data['password'], password)):
                session['login'] = True
                session['firstname'] = data['first_name']
                session['lastname'] = data['last_name']
                flash('Welcome '+ session['firstname'] +'! You have been successfully logged in', 'success')
                return redirect(url_for('dashboard'))
                cur.close()
            else:
                flash('Password incorrect', 'danger') 
                return redirect('login')
        else:
            flash('Username incorrect', 'danger')   
            return redirect('login')        
    return render_template('login.html')


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'GET':
        return render_template('forgot.html' )
    else:
        email = request.form.get('email')
        cursor = mysql.connection.cursor()
        resulValue = cursor.execute('SELECT * FROM user WHERE email=%s',[email])
        
        if resulValue >0: 
            data = cursor.fetchone()
            #token = data['password']
            print(data)
            token = str(uuid.uuid4())
            msg = Message( subject='Password Reset Requested Email Link', sender='demo@bestsolution.me', recipients=[email])
            link = url_for('password_confirm', token = str(uuid.uuid4()), _external=True )
            msg.body = render_template(  'sentmail.html', data=data, token=token, link=link)
            mail.send(msg) 
            flash('Email already sent to your mail','success') 
            return redirect(url_for('forgot')) 
        else:
            flash ('Email does not matched', 'danger')
            msg = Message( subject='Password Reset Requested Email Link', sender='demo@bestsolution.me', recipients=[email])
            msg.body = "This email does not exist in our system, " \
                       "if you not the one who entered this mail ignore this message. Please Registration"
            mail.send(msg) 
            return redirect(url_for('register'))
    

@app.route('/password_confirm', methods=['GET', 'POST'])
def password_confirm():
    if request.method == 'POST':
        verify = request.form['verify']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash('Passwords do not match! Try again.', 'danger')
            return redirect('password_confirm')
        password = bcrypt.generate_password_hash(password) 
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE password=%s',[verify])
        user = cursor.fetchone()
        if user: 
            cur = mysql.connection.cursor()
            cur.execute("UPDATE user SET password = %s  WHERE password=%s",(password, verify))
            mysql.connection.commit()
            cur.close()
            flash('Password updated successfully', 'success') 
            return redirect('login')
        else:  
            flash('verify code not match','danger') 
            return redirect('password_confirm')
           

    return render_template('reset_password.html')    

# Write a new blog
@app.route('/write-blog', methods=['GET', 'POST'])
def write_blog():
    if 'login' not in session:
        return redirect('/')
    if request.method == 'POST':
            author = session['firstname'] + ' ' + session['lastname']
            title = request.form['title']
            body = request.form['body']
            img = save_images(request.files['img'])
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO blog (title, img, body, author) VALUES (%s, %s, %s, %s)", (title, img, body, author))
            mysql.connection.commit()
            flash("Successfully posted new blog", 'success')
            return redirect('/')
  
    return render_template('write-blog.html')
     

@app.route('/my-blogs')
def view_blogs():
    if 'login' not in session:
        return redirect('/')
    author = session['firstname'] + ' ' + session['lastname']
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM blog WHERE author = %s",[author])
    if result_value > 0:
        my_blogs = cur.fetchall()
        return render_template('my-blogs.html',my_blogs=my_blogs)
    else:
        return render_template('my-blogs.html',my_blogs=None)
    
       #return render_template('my-blogs.html', post=post)
    
    

# Edit blog
@app.route('/edit-blog/<int:id>', methods=['GET', 'POST'])
def edit_blog(id):
    if 'login' not in session:
        return redirect('/')
    author = session['firstname'] + ' ' + session['lastname']
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        title = request.form['title']
        body = request.form['body']
        cur.execute("UPDATE blog SET title = %s, body = %s where blog_id = %s",(title, body, id))
        mysql.connection.commit()
        cur.close()
        flash('Blog updated successfully', 'success')
        return redirect('/blogs/{}'.format(id))
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM blog WHERE blog_id = {}".format(id))
    if result_value > 0:
        blog = cur.fetchone()
        return render_template('edit-blog.html', blog_form=blog)

@app.route('/edit-profile/<username>', methods=['GET', 'POST'])
def edit_profile(username):
    if 'login' not in session:
        return redirect('/')
    if request.method == 'POST':
        author = session['firstname'] + ' ' + session['lastname']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        img = save_images(request.files['img'])
        title = request.form['title']
        des = request.form['des']
       
        cur = mysql.connection.cursor()
        cur.execute("UPDATE user SET first_name =%s, last_name=%s, email=%s, img=%s, title=%s, des=%s where username=%s", (first_name, last_name, email, img, title, des, username))
        mysql.connection.commit()
        cur.close()
        flash('Profile updated successfully', 'success')
        return redirect('/dashboard')
      
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM user WHERE username =%s",[username])
    if result_value > 0:
        user = cur.fetchone()
       
        return render_template('edit_profile.html', user=user)     


@app.route('/changepassword/<username>', methods=['GET', 'POST'])
def changepassword(username):
    if request.method == 'POST':
        old = request.form['old']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash('Passwords do not match! Try again.', 'danger')
            return redirect('/dashboard')   
        password = bcrypt.generate_password_hash(password) 
        cur = mysql.connection.cursor()
        result_value = cur.execute("SELECT * FROM user WHERE username =%s",[username])
        if result_value > 0:
            user = cur.fetchone()
            if bcrypt.check_password_hash(user['password'], old):
                cur = mysql.connection.cursor()
                cur.execute("UPDATE user SET password = %s  WHERE username=%s",(password, username))
                mysql.connection.commit()
                cur.close()
                flash('Password updated successfully', 'success') 
                return redirect('/dashboard')
            else:
                flash('Old Password Incorrect', 'danger') 
                return redirect('/dashboard')       
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM user WHERE username =%s",[username])
    if result_value > 0:
        user = cur.fetchone()
        return render_template('changepassword.html', user=user)    
           

@app.route('/contactinfo', methods=['GET', 'POST'])
def update():
    author = session['firstname'] + ' ' + session['lastname']
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM contact WHERE author=%s",[author])
    if resultValue > 0:
        contact = cur.fetchall()
        cur.close()
        return render_template('change.html', contact=contact)
    cur.close()
    return render_template('change.html', contact=None)
    

@app.route('/delete-blog/<int:id>')
def delete_blog(id):
    if 'login' not in session:
        return redirect('/')
    author = session['firstname'] + ' ' + session['lastname']
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM blog WHERE blog_id = %s",[id])
    mysql.connection.commit()
    flash("Your blog has been deleted", 'success')
    return redirect('/my-blogs')

@app.route('/contactmove/<string:id>')
def contact_move(id):
    author = session['firstname'] + ' ' + session['lastname']
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM contact WHERE id={}".format(id))
    mysql.connection.commit()
    flash("Your message has been deleted", 'success')
    return redirect('/contactinfo')    
    

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out", 'info')
    return redirect('/')
    
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')

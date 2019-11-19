if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		usr_entered = request.form['password']
		cursor = mysql.connection.cursor()
		cursor.execute("SELECT * FROM user WHERE username =%s", [username])
		if cursor is not None: #is not None
			data =cursor.fetchone()
			#password = data['password']
			                                  # print((password))
			                                  # print((usr_entered))
			                                  # print((generate_password_hash(usr_entered , 'pbkdf2:sha256' , 8)))
			                                  # print(check_password_hash(password , usr_entered))
			                                  # check_password_hash(password , 'usr_entered')
			if (bcrypt.check_password_hash(data['password'] , usr_entered)):
				session['login'] = True 
				session['firstname'] = data['first_name']
				session['lastname'] = data['last_name']

				flash('Welcome '+ session['firstname'] +'! You have been successfully logged in', 'success')
				cursor.close()
			else:
				flash('Password Incorrect', 'danger')  
				return redirect('/login')
	return render_template('login.html')



from flask import Flask, render_template, redirect, url_for, request, flash, session, current_app
from blog import Bootstrap
from .models import User
from blog import app, mysql, mail , msg,bcrypt, db
from itsdangerous import URLSafeSerializer, SignatureExpired
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
import secrets
import os
from flask_mail import Mail, Message

msg = Message

s = URLSafeSerializer('secretthistime!')



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
		   

@app.route('/', methods=['GET','POST'])
def home():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM blog ORDER BY blog_id DESC")
    if resultValue > 0:
        blogs = cur.fetchall()
        cur.close()
        return render_template('index.html', blogs=blogs)
    cur.close()
    return render_template('index.html', blogs=None)
  

@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/', methods=['GET', 'POST'] )
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

@app.route('/blogs/<int:id>/')
def blogs(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM blog WHERE blog_id = {}".format(id))
    if resultValue > 0:
        blog = cur.fetchone()
        return render_template('blogs.html', blog=blog)
    return 'Blog not found'

    
    
   

@app.route('/register/', methods=['GET', 'POST'])
def register():
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
    return render_template('register.html')
@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method == 'POST' :
		username = request.form['username']
		usr_entered = request.form['password']
		cursor = mysql.connection.cursor()
		cursor.execute("SELECT * FROM user WHERE username =%s", [username])
		if cursor is not None: #is not None
			data =cursor.fetchone()
			#password = data['password']
			                                  # print((password))
			                                  # print((usr_entered))
			                                  # print((generate_password_hash(usr_entered , 'pbkdf2:sha256' , 8)))
			                                  # print(check_password_hash(password , usr_entered))
			                                  # check_password_hash(password , 'usr_entered')
			if (bcrypt.check_password_hash(data['password'] , usr_entered)):
				session['login'] = True 
				session['firstname'] = data['first_name']
				session['lastname'] = data['last_name']

				flash('Welcome '+ session['firstname'] +'! You have been successfully logged in', 'success')
				cursor.close()
			else:
				flash('Password Incorrect', 'danger')  
				return redirect('/login')
	return render_template('login.html')


@app.route('/forgot/', methods=['GET', 'POST'])
def forgot():
    if request.method == 'GET':
        return render_template('forgot.html' )
        email = request.form.get('email')
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE email=%s',[email])
        user = cursor.fetchone()
        if user: 
            flash('Email already sent to reset ','success') 
            token = s.dumps(email, salt='email-confirm')
            msg = Message(subject='Reset Mail', sender='admin@bestsolution.me ', recipients=[email])
            link = url_for('reset_password', token=token, _external=True)

            msg.body = render_template('reset_password.html', token=token, link=link)
            mail.send(msg) 
            return redirect(url_for('login')) 
        else:
            flash ('Email does not matched', 'danger')
    

    


@app.route('/reset_password/', methods=['GET', 'POST'])
def reset_password():
    return render_template('reset_password.html')    

# Write a new blog
@app.route('/write-blog/', methods=['GET', 'POST'])
def write_blog():
    author = session['firstname'] + ' ' + session['lastname']

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        img = save_images(request.files['img'])
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO blog (title, img, body, author) VALUES (%s, %s, %s, %s)", (title, img, body, author))
        mysql.connection.commit()
        flash("Successfully posted new blog", 'success')
        return redirect('/')
    return render_template('write-blog.html')
   
    

# View my blog
@app.route('/my-blogs/')
def view_blogs():
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
@app.route('/edit-blog/<int:id>/', methods=['GET', 'POST'])
def edit_blog(id):
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
        blog_form = {}
        blog_form['title'] = blog['title']
        blog_form['body'] = blog['body']
        return render_template('edit-blog.html', blog_form=blog_form)

@app.route('/edit-contact/<int:id>/', methods=['GET', 'POST'])
def edit_msg(id):
    author = session['firstname'] + ' ' + session['lastname']
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['msg']
        cur.execute("UPDATE contact SET name = %s, email = %s, subject = %s, msg = %s where id = %s",(name, email, subject, msg, id))
        mysql.connection.commit()
        cur.close()
        flash('Message updated successfully', 'success')
        return redirect('/')
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM contact WHERE id = {}".format(id))
    if result_value > 0:
        contact = cur.fetchone()
        contact_form = {}
        contact_form['name'] = contact['name']
        contact_form['email'] = contact['email']
        contact_form['subject'] = contact['subject']
        contact_form['msg'] = contact['msg']
        return render_template('edit-contact.html', contact_form=contact_form)        

@app.route('/contactinfo/', methods=['GET', 'POST'])
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
    

@app.route('/delete-blog/<int:id>/')
def delete_blog(id):
    author = session['firstname'] + ' ' + session['lastname']
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM blog WHERE blog_id = {}".format(id))
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
    

@app.route('/logout/')
def logout():
    session.clear()
    flash("You have been logged out", 'info')
    return redirect('/')
    
@app.errorhandler(404)
def page_not_found(e):
    return 'This page was not found for you'

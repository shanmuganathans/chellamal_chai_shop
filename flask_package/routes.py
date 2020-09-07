from flask import render_template,request,redirect,url_for,flash
from datetime import datetime
from flask_package.forms import RegisterationForm,LoginForm
from flask_package.models import User
#hash key generation
from flask_package import app,db,bcrypt
#session management
from flask_login import login_user,logout_user,current_user


feedback = []


# Pointing multiple url into same endpoint
@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template("index.html", new_feedback = new_feedback(3))

@app.route("/feedback",methods=["GET", "POST"])
def feedback_page():
    if request.method == 'POST':
        feedback_page = request.form['url']
        store_feedback(feedback_page)
        app.logger.debug('Feedback by the user %s' % feedback_page)
        app.logger.debug("stored feedback %s" % feedback)
        flash('user feedback: ' +feedback_page)
        return redirect(url_for('home_page'))
    return render_template("feedback.html")

@app.route('/login',methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash('login successfully..!')
            return redirect(url_for('home_page'))
        else:
            flash("Login unsuccessful.!")
        
    return render_template('login.html',title = 'Login Page', form = form)

@app.route('/register',methods=["GET", "POST"])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))

    form = RegisterationForm()
    # if form.validate():
    #     print( "valid")
    # if form.is_submitted():
    #     print("submitted")
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, email = form.email.data, password = hash_password)
        db.session.add(user)
        db.session.commit()
        flash("Account has created..!")
        return redirect(url_for('login_page'))
    if form.errors:
       print(form.errors)
    return render_template('regsiter.html',title = 'Register user',form = form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



def store_feedback(url):
    feedback.append(dict(
        url = url,
        user = 'test',
        date = datetime.utcnow()
    ))

def new_feedback(num):
    return sorted(feedback, key = lambda bm:bm['date'], reverse = True)[:num]

@app.route('/logout')
def logout():
    logout_user()
    flash("logout successfully..!")
    return redirect(url_for('home_page'))

@app.route('/sale')
def sale():
    return render_template('sale.html')
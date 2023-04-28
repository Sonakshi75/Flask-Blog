from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '9d9adc51c53446372463266bf2fc0955'
posts = [
{
'author':'Sonakshi Mugrai',
'title':'First Blog',
'content':'First post content',
'date_posted':'April 9, 2023'
},
{
'author':'Sagar Pandey',
'title':'Second Blog',
'content':'Second post content',
'date_posted':'April 10, 2023'
}
]

@app.route("/")
@app.route("/home")
def Home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title = "About")

@app.route("/register", methods = ['GET','POST'] )
def Register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}! ', 'success')
		return redirect(url_for('Home'))
	return render_template('register.html', title='register',form = form)

@app.route("/login", methods = ['GET','POST'])
def Login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@log.com' and form.password.data == 'password':
			flash(f'You have been logged in!','success')
			return redirect(url_for('Home'))
		else:
			flash('Login unsecessfull, please check username and password','danger')
	return render_template('login.html', title = 'login', form = form)
if __name__=="__main__":
	app.run(debug = True)

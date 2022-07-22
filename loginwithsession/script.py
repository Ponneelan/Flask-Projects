from requests import request
from flask import *


app = Flask(__name__)
app.secret_key = 'hi'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        session['email']=request.form['email']
        return render_template('success.html')
    else:
        return render_template('warn.html')
    
@app.route('/profile')
def profile():
    if 'email' in session:
        email= session['email']
    return render_template('profile.html',name = email)
    
        
    
@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email',None)
        return render_template('logout.html')
    else:
        return 'please login first'
    
if __name__ == '__main__':
    app.run(debug= True)
        
    
from crypt import methods
from distutils.log import debug

from requests import request
from flask import *

app = Flask(__name__)

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/success",methods=['POST'])
def afterlogin():
    
    if request.method == 'POST':
        email = request.form['email']
        upass = request.form['pass']
        
    if upass == 'vasanth':
        res = make_response(render_template("success.html"))
        res.set_cookie('email',email)
        return res
    else:
        return redirect(url_for('error'))
        
        
        
@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/profile')
def profile():
    email = request.cookies.get('email')
    res =  make_response(render_template('profile.html',name=email))
    return res


if __name__ == "__main__":
    app.run(debug=True , port = 5000)
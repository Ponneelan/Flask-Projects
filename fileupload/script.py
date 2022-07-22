from requests import request
from flask import *

app = Flask(__name__)

@app.route('/')  
def index():  
    return render_template("file_upload.html")  
  

@app.route('/upload',methods = ['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
    return render_template('uploaded.html',name = f.filename)


if __name__ == '__main__':
    app.run(debug=True)
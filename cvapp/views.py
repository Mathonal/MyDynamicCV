from flask import Flask, render_template, url_for

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

#Import cyclicity error if placed before App=
from .utils import find_comp

@app.route('/')
@app.route('/index/')
def index():

    return render_template('index.html')

def rendercv(Wkclass):
    #Wkclass = 'Data'
    myUrl = 'Bootstrap_CV&wk='+Wkclass+'.html'

    complist = find_comp(Wkclass)
    return render_template(myUrl,
                            type=Wkclass,
                            complist=complist)

@app.route('/CVdata/')
def datacv(): return rendercv('Data')

@app.route('/CVdev/')
def devcv():return rendercv('Dev')

@app.route('/CVeng/')
def engcv():return rendercv('Eng')
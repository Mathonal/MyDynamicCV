from flask import Flask, render_template, url_for

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

#Import cyclicity error if placed before App=
from .utils import find_tcomp,find_gcomp

#INDEX DISPLAY
@app.route('/')
@app.route('/index/')
def index():

    gcomplist = find_gcomp('DataDevEng')

    return render_template('index.html',
                            gcomplist=gcomplist)

#SPECIFIC DISPLAYS
def rendercv(Wkclass):
    #Wkclass = 'Data'
    myUrl = 'CV&wk='+Wkclass+'.html'

    tcomplist = find_tcomp(Wkclass)
    gcomplist = find_gcomp(Wkclass)

    return render_template(myUrl,
                            type=Wkclass,
                            tcomplist=tcomplist,
                            gcomplist=gcomplist)

# DISPLAYS
@app.route('/CVdata/')
def datacv(): return rendercv('Data')

@app.route('/CVdev/')
def devcv():return rendercv('Dev')

@app.route('/CVeng/')
def engcv():return rendercv('Eng')
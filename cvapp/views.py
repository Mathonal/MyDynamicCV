from flask import Flask, render_template, url_for
from flask import Blueprint

from .utils import find_tcomp,find_gcomp

# Blueprint
routes = Blueprint('routes', __name__,
        template_folder='templates',
        static_folder='static',
        static_url_path='/static')


#INDEX DISPLAY
@routes.route('/')
@routes.route('/index/')
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
@routes.route('/CVdata/')
def datacv(): return rendercv('Data')

@routes.route('/CVdev/')
def devcv():return rendercv('Dev')

@routes.route('/CVeng/')
def engcv():return rendercv('Eng')
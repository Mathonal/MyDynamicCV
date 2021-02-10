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

    return render_template('Page_index.html',
                            gcomplist=gcomplist)

# BLOG PAGE
@routes.route('/blog/')
def blogtest() : return render_template('Page_Post.html')


# ABOUT ME SECTION 
def rendercv(Wkclass):
    myUrl = 'Page_AboutMe.html'

    if Wkclass == 'All' : 
        gcomplist = find_gcomp('DataDevEng')
        tcomplist = None
    else :
        tcomplist = find_tcomp(Wkclass)
        gcomplist = find_gcomp(Wkclass)

    print(Wkclass)

    return render_template(myUrl,
                            type=Wkclass,
                            tcomplist=tcomplist,
                            gcomplist=gcomplist)

# specific CV DISPLAYS
@routes.route('/CVdata/')
def datacv(): return rendercv('Data')

@routes.route('/CVdev/')
def devcv():return rendercv('Dev')

@routes.route('/CVeng/')
def engcv():return rendercv('Eng')

# Global CV DISPLAY
@routes.route('/Me/')
def allcv(): return rendercv('All')
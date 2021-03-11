from flask import Flask, render_template, url_for
from flask import Blueprint

from .utils import find_tcomp,find_gcomp
import os
import mistune


def rootdir() : 
    return os.path.abspath(os.path.dirname(__file__))

def showdev() :
    if os.getenv('ISHEROKU') : return False
    else : return True

# Blueprint
routes = Blueprint('routes', __name__,
        template_folder='templates',
        static_folder='static',
        static_url_path='/static')


#INDEX DISPLAY
@routes.route('/')
@routes.route('/index/')
def index():

    #gcomplist = find_gcomp('DataDevEng')

    return render_template('Page_index.html',
                            showdev = showdev())

    return render_template('Page_index.html',
                            gcomplist=gcomplist, showdev = showdev())

# BLOG PAGES
@routes.route('/blog/')
def blogindex() :   
    return render_template('Page_indexblog.html', showdev = showdev())

@routes.route('/blog/myblogtest')
def blogtestpage() : 
    blogtitle = 'Test page'
    blogimgpath = 'img/thumb/pythoncode.png'

    # markdown file path (cvapp folder) 
    path = os.path.join(rootdir(),"templates/blog/Markdowntest.md")
    # get file content
    textmd = open(path, "r").read()
    # transform in HTML (with mistune) and return 
    return render_template('test/TestPage_blogpost_MD.html', textmd = mistune.html(textmd),
        blogtitle = blogtitle, blogimgpath = blogimgpath)

@routes.route('/blog/JupiterNotebookDockerContainer')
def blogpage1() :
    blogtitle = 'Easily Setup Docker Container and environnement \
        for DataScience with JupiterNotebook'
    blogimgpath = 'img/blog/jupyterdocker_intro.png'

    # MD FILE
    path = os.path.join(rootdir(),"templates/blog/JupyterDockerImage.md")
    textmd = open(path, "r").read()
    # transform in HTML (with mistune) and return 
    return render_template('Page_blogpostmarkdown_template.html', textmd = mistune.html(textmd),
        blogtitle = blogtitle, blogimgpath = blogimgpath)

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
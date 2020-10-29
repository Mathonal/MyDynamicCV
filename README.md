# MyDynamicCV
webdesign of CV with python flask

Application designed to run with WebApp Azure Services
Use Flask and Sqlite for dynamic display
use docker flaskserver when working on branching (instructions in dockerfile)

### Specific Sql process for this app 
(needed because app root folder on Azure is lock on read-only:https://github.com/Azure/app-service-announcements/issues/84):

**1.** in cvapp/__init__.py, there is SQLPOPULATE_AT_STARTUP variable that MUST BE on FALSE when app is deployed on GIT/MAIN (and syncronised to Azure) !!
(if app tries to update app.DB in azure >> crash)

**2.** SQLPOPULATE_AT_STARTUP on True is designed to modify/populate the SQL app.db file on Local repository (with local container), or non azure deployed branch.
this allow to modify app.db file content on the fly via MODELS.py

## GENERIC DESCRIPTION OF FILES:

### ROOT:
**app.py** : launch app. (must keep this name to be recognized bu AzureWebApp)

**app.db**: sql db containing ordered data to populate html pages. find content details in cvapp/models.py

**config.py** : contains some init variable for sqlite

**dockerfile** : for creating a flask container when working on local branching. (contains comment section with docker command to build/run)

**requirements** : list of libraries to install (used by Docker/build AND AzureWebApp)

### APP ROOT:
**models.py** : define and/or populate database used in technical skill definition parts
        currently 1 DB : CompGraph(id, name, type, percentvalue)

**utils.py** : functions that parse DB

**views.py** : functions that render html pages
        currently 4 pages : index, CVData, CVEng, CVDev



### TEMPLATE FOLDER:
**index.html, Bootstrap_CV&wk=Data.html, Bootstrap_CV&wk=Eng.html, Bootstrap_CV&wk=Dev.html** : *4 main pages of the CV.* Calls to all following HTML cards when rendered with views.py

**base.html (card)** : contains header and footer layout of pages

**missions (card)** : contains detailled missions layout, with filter on WorkType

**skillgraph (card)** : contains layout of technical skill section. it work with a screening of the app.db with an utils functions

**skillglobal (card)** : contains more project oriented skill, *just HTML code*

**workxp (card)** : contains sections about work / businesses / duration, *just HTML code*


### STATIC FOLDER:
**CSS** : contains BOOTSTRAP CSS file and my personnal css file for this app : STYLE.CSS & GRID_DISPLAY.CSS

**IMG** : contains ressources

**JS** : contains BOOTSTRAP JS SCRIPTS.
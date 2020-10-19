# MyDynamicCV
webdesign of CV with python flask

Application design to run with WebApp Azure Services
Use Flask and Sqlite for dynamic display

Specific Sql process for this app 
(needed because app root folder on Azure is lock on read-only:https://github.com/Azure/app-service-announcements/issues/84):
1- in cvapp/__init__.py, there is SQLPOPULATE_AT_STARTUP variable that MUST BE on FALSE when app is deployed on GIT/MAIN (and syncronised to Azure) !!

2- SQLPOPULATE_AT_STARTUP on True is design to modify the SQL app.db file on Local repository (with local container), or non azure deployed branch.
this allow to modify app.db file content on the fly via MODELS.py


GENERIC DESCRIPTION OF FILES:

ROOT:
    Models : define and/or populate database used in technical skill definition parts
        currently 1 DB : CompGraph(id, name, type, percentvalue)

    utils : functions that parse DB

    views : functions that render html pages
        currently 4 pages : index, CVData, CVEng, CVDev

TEMPLATE FOLDER:
    index.html, Bootstrap_CV&wk=Data.html, Bootstrap_CV&wk=Eng.html, Bootstrap_CV&wk=Dev.html : 4 main pages of the CV

    base.html : contains header en footer of pages

    missions : contains detailled missions, with filter on WorkType

    skillgraph : contains card for graphical display of technical skill. it work with a screening of the app.db with an utils functions

    skillglobal : contains more project oriented skill, just HTML code

    workxp : contains sections about work / businesses / duration, just HTML code


STATIC FOLDER:
    CSS : contains BOOTSTRAP CSS file 
    and my personnal css file for this app : STYLE.CSS & GRID_DISPLAY.CSS

    IMG : contains ressources

    JS : contains BOOTSTRAP JS SCRIPTS.
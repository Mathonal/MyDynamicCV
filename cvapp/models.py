from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

from .views import app
# Create database connection object
db = SQLAlchemy(app)

class WorkClass(enum.Enum):
    Data = 1
    Dev = 2
    Eng = 4
    DataDev = 3
    DataEng = 5
    DevEng = 6
    DataDevEng = 7

class CompGraph(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    wc = db.Column(db.Enum(WorkClass), nullable=False)
    percentvalue = db.Column(db.Integer, nullable=False)

    def __init__(self, name, workclass, percentvalue):
        self.name = name
        self.wc = workclass
        self.percentvalue = percentvalue

def init_compgraphdb():
    #MULTI COMP
    db.session.add(CompGraph("Python", WorkClass['DataDev'],95))
    db.session.add(CompGraph("Microsoft Azure", WorkClass['DataDev'],75))
    db.session.add(CompGraph("CATIA Knowledge", WorkClass['DevEng'],95))

    #DATA COMP
    db.session.add(CompGraph("Spark", WorkClass['Data'],95))
    db.session.add(CompGraph("Hadoop Env", WorkClass['Data'],85))
    db.session.add(CompGraph("Talend ETL", WorkClass['Data'],95))
    db.session.add(CompGraph("Tableau", WorkClass['Data'],90))
    db.session.add(CompGraph("Tensorflow / Scikit", WorkClass['Data'],90))
    db.session.add(CompGraph("Kafka", WorkClass['Data'],75))
    db.session.add(CompGraph("SQL", WorkClass['Data'],95))
    db.session.add(CompGraph("NoSQL Cassandra", WorkClass['Data'],75))

    #DEV COMP
    db.session.add(CompGraph("Unix Shell", WorkClass['Dev'],95))
    db.session.add(CompGraph("HTML5/CSS3", WorkClass['Dev'],85))
    db.session.add(CompGraph("Flask/Bootstrap", WorkClass['Dev'],65))
    db.session.add(CompGraph(".NET/VBA", WorkClass['Dev'],90))
    db.session.add(CompGraph("C++", WorkClass['Dev'],50))
    db.session.add(CompGraph("JAVA", WorkClass['Dev'],50))

    #ENG COMP
    db.session.add(CompGraph("CATIA/GDT", WorkClass['Eng'],95))
    db.session.add(CompGraph("Nastran", WorkClass['Eng'],95))
    db.session.add(CompGraph("Abaqus", WorkClass['Eng'],75))
    db.session.add(CompGraph("ANSA", WorkClass['Eng'],85))
    db.session.add(CompGraph("Altair Optistruct", WorkClass['Eng'],75))
    db.session.add(CompGraph("Simulia Isight", WorkClass['Eng'],95))
    db.session.add(CompGraph("Vrand Genesis", WorkClass['Eng'],95))
    db.session.add(CompGraph("Vrand VisualDoc", WorkClass['Eng'],95))


class CompGlob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    wc = db.Column(db.Enum(WorkClass), nullable=False)
    short = db.Column(db.String(200), nullable=False)

    def __init__(self, name, workclass, short):
        self.name = name
        self.wc = workclass
        self.short = short

def init_compglobdb():
    #MULTI COMP
    db.session.add(CompGlob("Audit de Processus", WorkClass['DataDevEng'],
        "Comprendre et analyser avec précision les besoins d'un client. \
        Realiser des spécifications techniques détaillées."))

    db.session.add(CompGlob("Etude de faisabilité & chiffrage", WorkClass['DataDevEng'],
        "Verifier la capacité des outils à remplir un besoin client; \
        en chiffrer l'installation / l'execution."))

    db.session.add(CompGlob("Pilotage projet", WorkClass['DataDevEng'],
        "Suivre le developpement d'une application ou l'execution d'une étude"))

    db.session.add(CompGlob("Veille technologique", WorkClass['DataDevEng'],
        "Tenir ses compétences à jour. Surveiller le versionnement de ses \
        produits et ceux de la concurrence"))

    db.session.add(CompGlob("Présentation ", WorkClass['DataDevEng'],
        "Etre capable de rediger et présenter ses resultats via supports graphiques : Dashboard / powerpoint"))

    db.session.add(CompGlob("Formation & encadrement ", WorkClass['DataDevEng'],
        "Etre capable de rediger et dispenser des formations. Transmettre ses compétences "))

    # Specific comp
    # Ing
    db.session.add(CompGlob("Expertise CATIA/CAO", WorkClass['Eng'],
        "Etre capable de faire de la conception rejouable; Squeleton/topdown method. Manipulation surfacique avancée. \
        Inclusion de règles/verifications de conception (Knowledge)"))

    db.session.add(CompGlob("Expertise Conception additive", WorkClass['Eng'],
        "utilisation et interprétation d'optimisation topologique sur volume de conception"))



def init_db():
    db.drop_all()
    db.create_all()

    init_compgraphdb()
    init_compglobdb()

    db.session.commit()
    lg.warning('Database initialized!')
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


def init_db():
    db.drop_all()
    db.create_all()

    init_compdb()

    # db.session.add(CompGraph("TESTCOMP1", WorkClass['Data'],50))
    # db.session.add(CompGraph("TESTCOMP2", WorkClass['Dev'],50))
    # db.session.add(CompGraph("TESTCOMP3", WorkClass['Eng'],50))
    # db.session.add(CompGraph("TESTCOMP4", WorkClass['DataDev'],50))
    # db.session.add(CompGraph("TESTCOMP5", WorkClass['DataEng'],50))
    # db.session.add(CompGraph("TESTCOMP6", WorkClass['DevEng'],50))    
    # db.session.add(CompGraph("TESTCOMP7", WorkClass['DataDevEng'],50))
    db.session.commit()
    lg.warning('Database initialized!')


def init_compdb():
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
from flask_sqlalchemy import SQLAlchemy
import logging
import enum

from . import db

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
    db.session.add(CompGraph("Microsoft Azure", WorkClass['DataDev'],65))
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
    img = db.Column(db.String(50), nullable=True)
    wc = db.Column(db.Enum(WorkClass), nullable=False)
    short = db.Column(db.String(200), nullable=False)

    def __init__(self, name, workclass, short, img=None):
        self.name = name
        self.wc = workclass
        self.short = short
        self.img = img

def init_compglobdb():
    #MULTI COMP
    db.session.add(CompGlob("Audit / Receuil de besoins", WorkClass['DataDevEng'],
        "Comprendre et analyser avec précision les besoins d'un client. \
        Realiser des spécifications techniques détaillées.",
        "img/processus.png"))

    db.session.add(CompGlob("Etude de faisabilité & chiffrage", WorkClass['DataDevEng'],
        "Verifier la capacité des outils à remplir un besoin client; \
        en chiffrer l'installation / l'exécution.",
        "img/faisabilite.png"))

    db.session.add(CompGlob("Organisation et conduite de réunions", WorkClass['DataDevEng'],
        "Maitriser les différents types de réunions (revue, échange, résolution), \
        adapter ses ordres du jours, et avoir des objectifs clairs",
        "img/reunion.png"))

    db.session.add(CompGlob("Pilotage projet", WorkClass['DataDevEng'],
        "Suivre le développement d'une application ou l'exécution d'une étude",
        "img/pilotage.png"))

    db.session.add(CompGlob("Veille technologique", WorkClass['DataDevEng'],
        "Tenir ses compétences à jour. Surveiller le versionnement de ses \
        produits et ceux de la concurrence",
        "img/veille.png"))

    db.session.add(CompGlob("Présentation ", WorkClass['DataDevEng'],
        "Etre capable de rédiger et présenter ses résultats via supports graphiques : Dashboard / powerpoint",
        "img/presentation.jpg"))

    db.session.add(CompGlob("Formation & encadrement ", WorkClass['DataDevEng'],
        "Etre capable de rédiger et dispenser des formations. Transmettre ses compétences",
        "img/formation.jpg"))


    # Specific comp : Ing
    db.session.add(CompGlob("Expertise CATIA/CAO", WorkClass['Eng'],
        "Etre capable de faire de la conception rejouable; Squeleton/topdown method. \
        Inclusion de règles/vérifications de conception (Knowledge); surfacique avancée",
        "img/catia.jpg"))

    db.session.add(CompGlob("Expertise Conception additive", WorkClass['Eng'],
        "Utilisation et interprétation d'optimisation topologique sur volume de conception. Interpretation de résultats, \
        prise en comptes de contraintes de conception. Rédaction/présentation de DataStories sur campagne de calculs",
        "img/topologicaloptim.png"))

    db.session.add(CompGlob("Expertise optimisation paramétrique", WorkClass['Eng'],
        "Construction de workflows de calculs couplées à des algorithmes d'optimisation",
        "img/optimparametriqueflow.png"))

    db.session.add(CompGlob("Data Mining", WorkClass['Eng'],
        "Exploration de domaine (Plan d'expériences) ; Choix d'algorithme de calculs & paramètres;\
         Data-Mining & Regression ; Insight paramètres principaux & effet de couplage ; Statistique inférentielle \
         & probabilités de mise en défaut de pièces",
        "img/surfacereponse.png"))


    # Specific comp : Data
    db.session.add(CompGlob("Python Advanced", WorkClass['Data'],
        "Développement objets & exploratoire (Jupyter) ; structures avancées / factorisation ; APIs",
        "img/thumb/pythoncode.png"))

    db.session.add(CompGlob("Maitrise librairies Data-Science : Machine learning / Deep learning", WorkClass['Data'],
        "Appliquer des algorithmes exploratoires et statistiques descriptives, \
        choix et utilisation des bibliothèques d’algorithmes d'IA issues \
        de solutions de références pour appliquer des modèles de qualification/projections/prédictions. \
        (Jupyterlab; Pandas ; Numpy ; SciKit ; Keras-Tensorflow ; Matplotlib SeaBorn ; Statsmodels",
        "img/thumb/net_ml.png"))

    db.session.add(CompGlob("Maitrise des outils ETL (Extract, Transform, and Load)", WorkClass['Data'],
        "Création de Pipeline ETL / Dataflow a partir de sources multiples et hétérogènes (Talend) ;\
        Contrôle des paradigmes de l’ingestion et du streaming de données. (Talend/Kafka)",
        "img/thumb/ETL_talend.png"))

    db.session.add(CompGlob("Charger, qualifier, nettoyer les données structurées ou non structurées", WorkClass['Data'],
        " Création de sets de données structurées et DataWarehouse à partir de DataLake (Python, Spark)",
        "img/thumb/datacleaning.png"))


    db.session.add(CompGlob("Restituer des données - Data Visualisation", WorkClass['Data'],
        "Dashboard & Data story sous logiciel dédié Tableau / powerBI ou via developpement web via \
        Framework Flask/Python plotli. Reporting statique via HTML-pdf",
        "img/thumb/dashboard.png"))

    db.session.add(CompGlob("Maitrise outils stockage et traitement BIGDATA", WorkClass['Data'],
        "Environnement stockage Hadoop, Calculs distribués avec Spark, Datawarehouse avec Hive",
        "img/thumb/spark.png"))
    
    # Specific comp : Dev
    db.session.add(CompGlob("Maitrise la programmation objet", WorkClass['Dev'],
        "Realisation de plusieurs projets (professionnel & personnel) reposant sur l'utilisation et la manipulation de classes & heritage",
        "img/thumb/poo.png"))
    db.session.add(CompGlob("Maîtrise les outils de Content Management System & Framework", WorkClass['Dev'],
        "Essentiel pour une bonne maitrise de sa configuration, accélerer faciliter son projet avec des outils spécialisés. \
        framework .NET, Anaconda Flask JupyterLab pour le python, Bootstrap et Bulma pour le CSS",
        "img/thumb/framework.png"))
    db.session.add(CompGlob("Maîtrise des outils de versionnement (GIT) et industrialisation (Docker/Cloud-Plateforme)", WorkClass['Dev'],
        "Publie régulièrement des mises à jours de mes projets GIThub lié à des web App PaaS/IaaS, ainsi que les évolutions de mes containers",
        "img/thumb/gitdocker.png"))
    db.session.add(CompGlob("Maîtrise des concepts de debugging - tests associés à un developpement", WorkClass['Dev'],
        "Publie régulièrement des mises à jours de mes projets GIThub lié à des web App PaaS/IaaS, ainsi que les évolutions de mes containers",
        "img/thumb/testDD.png"))    

def init_db():
    logging.warning('repopulating SQLDB')
    db.drop_all()
    db.create_all()

    init_compgraphdb()
    init_compglobdb()

    db.session.commit()
    logging.warning('Database initialized!')
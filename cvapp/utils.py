from .models import CompGraph, WorkClass

def find_comp(workclass):
    #look in DB and gets all item by workclass
    
    # All comp
    complist = CompGraph.query.filter(
        CompGraph.wc == WorkClass['DataDevEng']).all()
    
    #COMPOSE
    if workclass == 'Data' or workclass == 'Dev':
        complist += CompGraph.query.filter(
            CompGraph.wc == WorkClass['DataDev']).all()
    if workclass == 'Data' or workclass == 'Eng':
        complist += CompGraph.query.filter(
            CompGraph.wc == WorkClass['DataEng']).all()
    if workclass == 'Dev' or workclass == 'Eng':
        complist += CompGraph.query.filter(
            CompGraph.wc == WorkClass['DevEng']).all()
       
        #BASE 
    complist += CompGraph.query.filter(
        CompGraph.wc == WorkClass[workclass]).all()
    #contents = Content.query.filter(Content.gender == Gender[gender]).all()
    return complist
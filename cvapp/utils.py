from .models import WorkClass,CompGraph,CompGlob

def find_tcomp(workclass):
    #look in DB and gets all item by workclass
    if workclass == 'All' : return CompGraph.query.all()

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


def find_gcomp(workclass):
    #look in DB and gets all item by workclass
    #BASE
    if workclass == 'All' :
        return CompGraph.query.filter(
            CompGlob.wc == WorkClass['DataDevEng']).all()
    else :
        complist = CompGlob.query.filter(
            CompGlob.wc == WorkClass[workclass]).all()
        # Do not want All comp
        #complist = CompGraph.query.filter(
        #    CompGraph.wc == WorkClass['DataDevEng']).all()
        
        #COMPOSE
        if workclass == 'Data' or workclass == 'Dev':
            complist += CompGlob.query.filter(
                CompGlob.wc == WorkClass['DataDev']).all()
        if workclass == 'Data' or workclass == 'Eng':
            complist += CompGlob.query.filter(
                CompGlob.wc == WorkClass['DataEng']).all()
        if workclass == 'Dev' or workclass == 'Eng':
            complist += CompGlob.query.filter(
                CompGlob.wc == WorkClass['DevEng']).all()
           
        return complist
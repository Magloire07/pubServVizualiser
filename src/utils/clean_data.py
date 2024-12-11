import pandas as pd 
import json
from statistics import mean 


data= pd.read_csv("../../data/raw/labouref-france-departement-quarter-jobseeker.csv",sep=";")

periodes= data["Période (Trimestre)"].apply(lambda x: x[:4])
categories = data["Catégorie"]

listUniquePeriode=     sorted(set(periodes))
listUniqueCategories=  sorted(set(categories))

listSommeNbDemEmp=[]
for cat in listUniqueCategories:
    print(cat)
    data_by_cat= data[ data["Catégorie"] == cat ] # on extraite  les  observations par catégories
    for  p in listUniquePeriode:
        # on extrait et somme les nombre de demandeur  d'emploie par periode
        listSommeNbDemEmp.append( mean((data_by_cat[ (data_by_cat["Période (Trimestre)"].apply(lambda x: x[:4])==p)])["Nb moyen demandeur emploi"]))
    dico_by_cat= {"periodes":listUniquePeriode, "nombre_demandeur_emploi":listSommeNbDemEmp}
    # on écrit au format json les données à afficher en fonction des catégories 
    with open(f"../../data/cleaned/listSommecat_{cat}.json","w") as file:
        json.dump(dico_by_cat, file, indent=4, ensure_ascii=False)
    listSommeNbDemEmp=[] # on vide pour la prochaine catégorie




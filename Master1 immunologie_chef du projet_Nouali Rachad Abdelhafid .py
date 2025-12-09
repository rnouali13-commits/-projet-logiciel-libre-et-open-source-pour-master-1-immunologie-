#Salem c'est Mme Dib et Mr Ameur...c'est bien continue
#Pour que les membres puissent modifier il doivent appyer sur le stylo vert à droite et
#quand ils finissent ils doivent enregistrer sur commit changes pour enregistrer

#le chef de groupe: Nouali Rachad Abdelhafid /master1 immunologie/la date:06/12/2025
#REGUIEG ISSAAD Chaimaa 
#BERRANI AMINA 
#METAIR CHAIMAA
#NEGADI AMEL NASSIMA
#CHEKROUN ALAA SARA
import pandas as pd
data = {
    "Séquence":["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"],
    "longueur":[12,12,12,10,11,10,10],
    "pourcentage GC":[50,66.67,58.33,40,45.45,60,50],
}
# la première question:  Création  et afficher le tableau des séquence et longueur et pourcentage d'ADN
#Creation d'un dataFram (Tableau pandas)
tableau= pd.DataFrame(data)
print(" ***************création et affichage***************")

# Affichage du tableau 
print("Tableau des séquences ADN :" )
print(tableau)


















#la cinquième question: Ajouter une colonne de “Catégorie GC”
print("5/***l'ajoute d'une nouvelle colonne de catégorie GC***")
tableau["catégorie GC"]=tableau["pourcentage GC"].apply(lambda x:"Riche" if x > 55 else("Moyen" if 45<= x <= 55 else "Faible" ))
print(tableau,"\n")









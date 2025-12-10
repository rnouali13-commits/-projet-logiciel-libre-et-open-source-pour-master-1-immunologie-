#Salem c'est Mme Dib et Mr Ameur...c'est bien continue
#Pour que les membres puissent modifier il doivent appyer sur le stylo vert à droite et
#quand ils finissent ils doivent enregistrer sur commit changes pour enregistrer

#le chef de groupe: Nouali Rachad Abdelhafid /master1 immunologie/la date:06/12/2025
#REGUIEG ISSAAD CHAIMAA
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
#Afficher le résultat 
print(tableau, "\n")
import pandas as pd

# la deuxième question: Affichager la colonne de longueur sur un tableau
print(" **************2/ tableau de longueur************** ")

# Création du DataFrame
df = pd.DataFrame(tableau)  


# Affichager uniquement la colonne de longueur sur un tableau
Séquence = tableau ["longueur"]
print(Séquence , "\n")



# la troisième question :Filtrer les séquences dont la longueur est supérieure à 10
tableau= pd.DataFrame(data) 
print("**************3\Filtrage avec longueur**************")
filtered_tableau = tableau[tableau["longueur"]<10 ]   
#Afficher le résultat 
print(filtered_tableau,"\n")


      
     



















#la cinquième question: Ajouter une colonne de “Catégorie GC”
print("5/***l'ajoute d'une nouvelle colonne de catégorie GC***")
# Création du DataFrame
df = pd.DataFrame(tableau)  
tableau["catégorie GC"]=tableau["pourcentage GC"].apply(lambda x:"Riche" if x > 55 else("Moyen" if 45<= x <= 55 else "Faible" ))
#afficher le résultat
print(tableau,"\n")






# la septième question: Calculer l'écart-type du %GC et de la longueur des séquences

Average_gc = tableau["pourcentage GC"].std()



print(f"l'ecart type de GC:{average_gc:.3f}%")

# la huitiéme question : Sauvegarder le tableau final dans un fichier CSV 
# Afficher le résultat 






















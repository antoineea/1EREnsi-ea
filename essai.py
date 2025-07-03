import csv
fic = open("peintres.csv", "r", encoding="utf-8")
rdr = csv.DictReader(fic)	
							# DictReader, méthode (fonction) du module csv
							#   qui récupère le contenu sous forme complexe
							#   compatible du format de dictionnaires
tDic = list(rdr)			
							# list, une fonction qui convertit le contenu
							#   sous forme de liste (ici liste de
							#   dictionnaires)
fic.close()			
							# close, méthode qui ferme le fichier fic

for x in tDic :
	x["jour"] = int(x["jour"])
	x["mois"] = int(x["mois"])
	x["année"] = int(x["année"])
 
print (tDic)
for i in tDic:
    print(i['prenom'],i['nom'],"a réalisé ", i['tableau']," en ", i['année'])
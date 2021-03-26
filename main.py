import csv


##### version 1 ####

f = open("chiffres-cles.csv","r")
chiffres_covid = f.read()
chiffres_covid = chiffres_covid.split("\n")


tableau =[]

for row in chiffres_covid:
    split_row =row.split(",")
    tableau.append(split_row)


#date 0,granularite 1,maille_code 2,maille_nom 3,cas_confirmes 4,cas_ehpad 5,cas_confirmes_ehpad 6,cas_possibles_ehpad 7,deces 8,deces_ehpad 9,reanimation 10,hospitalises 11,nouvelles_hospitalisations 12,nouvelles_reanimations 13,gueris 14,depistes 15,source_nom,source_url,source_archive,source_type


print("Choissisez les chiffres que vous voulez voir")
print("\n")
print("\n")
print("cas_confirmes 4,cas_ehpad 5,cas_confirmes_ehpad 6,cas_possibles_ehpad 7,deces 8,deces_ehpad 9,reanimation 10,hospitalises 11,nouvelles_hospitalisations 12,nouvelles_reanimations 13,gueris 14,depistes 15")
print("\n")

n = int(input("Choisissez un chiffre entre 4 et 15 : "))
chiffres =0
ta = ""
dates = ""
howmani = 0
for i in tableau:
  if i[n].isdigit():
    i[n]= int(i[n])
    if int(i[n]) > chiffres:
      chiffres = i[n]
  if isinstance(i[n],str):
    ta += i[n]

for i in tableau:
  o = i[0]
dates = o




print(" Au")
print(dates,"\n","il y a ",chiffres,ta)
print("en France")

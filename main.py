import csv

class Covid_chiffre():
  def __init__(self):
    f = open("chiffres-cles.csv")
    chiffres_covid = csv.reader(f)
    self.chiffres_covid = list(chiffres_covid)

# methode qui creer plusieurs listes.
  def data_covid(self):
    date_cov = []
    granularite_cov =[]
    maille_code_cov = []
    maille_nom_cov = []
    cas_confirmes_cov = []
    cas_ehpad_cov = []
    cas_confirmes_ehpad_cov = []
    cas_possibles_ehpad_cov = []
    deces_cov = []
    deces_ehpad_cov = []
    reanimation_cov = []
    hospitalises_cov = []
    nouvelles_hospitalisations_cov = []
    nouvelles_reanimations_cov = []
    gueris_cov = []
    depistes_cov = []
    source_nom_cov = []
    source_url_cov = []
    source_archive_cov = []
    source_type_cov = []

    for i in self.chiffres_covid:
      date_cov.append(i[0])
      granularite_cov.append(i[1])
      maille_code_cov.append(i[2])
      maille_nom_cov.append(i[3])
      cas_confirmes_cov.append(i[4])
      cas_ehpad_cov.append(i[5])
      cas_confirmes_ehpad_cov.append(i[6])
      cas_possibles_ehpad_cov.append(i[7])
      deces_cov.append(i[8])
      deces_ehpad_cov.append(i[9])
      reanimation_cov.append(i[10])
      hospitalises_cov.append(i[11])
      nouvelles_hospitalisations_cov.append(i[12])
      nouvelles_reanimations_cov.append(i[13])
      gueris_cov.append(i[14])
      depistes_cov.append(i[15])
      source_nom_cov.append(i[16])
      source_url_cov.append(i[17])
      source_archive_cov.append(i[18])
      source_type_cov.append(i[19])

    self.data_cov = [set(date_cov[0:]),set(granularite_cov[0:]),set(maille_code_cov[0:]),set(maille_nom_cov[0:]),cas_confirmes_cov[0:],cas_ehpad_cov[0:],cas_confirmes_ehpad_cov[0:],cas_possibles_ehpad_cov[0:],deces_cov[0:],reanimation_cov,hospitalises_cov[0:],nouvelles_hospitalisations_cov[0:],nouvelles_reanimations_cov[0:],gueris_cov[0:],depistes_cov[0:],set(source_nom_cov[0:]),set(source_url_cov[0:]),set(source_archive_cov[0:]),set(source_type_cov[0:])]

    data_cov = self.data_cov
    return(self.data_cov)





  def deces(self):
    mort = []
    
    for row in self.chiffres_cov:
      try:
        mort.append(int(chiffres_covid[8]))
      except :
        mort.append(0)
    
    return(mort)











f = open("chiffres-cles.csv")
chiffres_covid = csv.reader(f)
chiffres_covid = list(chiffres_covid)


#variable pour verifier que ma methode ce balade bien dans les listes
Covid19 = Covid_chiffre()
listes = Covid19.data_covid()
#print(chiffres_covid[0])


int_listes = []
sujet = ""
for i in chiffres_covid:
  if i[8].isdigit():
    int_listes.append(int(i[8]))

  else:
    if i[8] in ("date","granularite","maille_code","maille_nom","cas_confirmes","cas_ehpad","cas_confirmes_ehpad","cas_possibles_ehpad","deces","deces_ehpad","reanimation","hospitalises","nouvelles_hospitalisations","nouvelles_reanimations","gueris","depistes","source_nom","source_url","source_archive","source_type"):
      print(i[8])
    sujet= i[8]


print(sum(int_listes),sujet)

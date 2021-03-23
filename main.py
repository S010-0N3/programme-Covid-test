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

    data_cov = [set(date_cov[0:]),set(granularite_cov[0:]),set(maille_code_cov[0:]),set(maille_nom_cov[0:]),set(cas_confirmes_cov[0:]),set(cas_ehpad_cov[0:]),set(cas_confirmes_ehpad_cov[0:]),set(cas_possibles_ehpad_cov[0:]),set(deces_cov[0:]),set(reanimation_cov[0:]),set(hospitalises_cov[0:]),set(nouvelles_hospitalisations_cov[0:]),set(nouvelles_reanimations_cov[0:]),set(gueris_cov[0:]),set(depistes_cov[0:]),set(source_nom_cov[0:]),set(source_url_cov[0:]),set(source_archive_cov[0:]),set(source_type_cov[0:])]
    return(data_cov)


Covid19 = Covid_chiffre()



#variable pour verifier que ma methode ce balade bien dans les listes
listes = Covid19.data_covid()
print(listes[8])
# -*- coding: utf-8 -*-

from collections import namedtuple

Instruccions = namedtuple('Instruccions', 'vells p aprof comment tipus')

class Xlate:

  # Nom de la plantilla destí
  nom_final = 'Infotaula persona'

  # el primer de la llista indica:
  # S: s'han d'esborrar per sistema la majoria de paràmetres. Només es
  #    conserven els que es tracten a la funció ...
  # N: els paràmetres s'han de traduir, però no fer una neteja bèstia
  plant = { 
	  'Infotaula persona':[('S','','')],
	  'Infotaula artista':[('S','','')],
	  'Infotaula d\'artista':[('S','','')],
	  'Infotaula Persona':[('S','','')],
	  'Compositor clàssic':[('S','','')],
	  'Infotaula de nedador':[('S','','')],
	  'Fitxa de persona':[('S','','')],
	  'Infotaula de persona':[('S','','')],
	  'Persona':[('S','','')],
	  'Infotaula de polític':[('S','','')],
	  'Infotaula d\'escriptor':[('S','','')],
	  'Persona de rellevància espiritual':[('S','','')],
	  'Infotaula Polític':[('S','','')],
	  'Infotaula polític':[('S','','')],
	  'Infotaula de músic':[('S','','')],
	  'Infotaula músic':[('S','','')],
	  'Músic':[('S','','')]
	}

  params = {    # a l'esquerra, el nom resultat, a la dreta, la llista de paràmetres que se substituiran pel de l'esquerra
	   'nom':			Instruccions(['Name','name'],'','',[],""),
	   'prefix_honorific':		Instruccions([],'','',[],''),
	   'sufix_honorific':		Instruccions([],'','',[],''),
	   'imatge':			Instruccions([],'','',[],''),
	   'peu':			Instruccions([],'','',[],''),
	   'alt':			Instruccions([],'','',[],''),
	   'nom_original':		Instruccions([],'','',[],''),
	   'nom_original_lleng':	Instruccions([],'','',[],''),
	   'nom_temple':		Instruccions([],'','',[],''),
	   'nom_postum':		Instruccions([],'','',[],''),
	   'nom_naixement':		Instruccions([],'','',[],''),
	   'lloc_naixement':		Instruccions([],'','',[],''),
	   'data_naixement':		Instruccions(['birth'],'','',[],''),
	   'bateig':			Instruccions([],'','',[],''),
	   'floruit':			Instruccions([],'','',[],''),
	   'lloc_defuncio':		Instruccions([],'','',[],''),
	   'data_defuncio':		Instruccions([],'','',[],''),
	   'causa_defuncio':		Instruccions([],'','',[],''),
	   'descobriment_cos':		Instruccions([],'','',[],''),
	   'data_desaparicio':		Instruccions([],'','',[],''),
	   'sepultura':			Instruccions([],'','',[],''),
	   'coordenades_sepultura':	Instruccions([],'','',[],''),
	   'residencia':		Instruccions([],'','',[],''),
	   'nacionalitat':		Instruccions([],'','',[],''),
	   'ciutadania':		Instruccions([],'','',[],''),
	   'altres noms':		Instruccions([],'','',[],''),
	   'alies':			Instruccions([],'','',[],''),
	   'nom_ploma':			Instruccions([],'','',[],''),
	   'etnia':			Instruccions([],'','',[],''),
	   'ideologia':			Instruccions([],'','',[],''),
	   'religio':			Instruccions(['religió'],'','',[],''),
	   'educacio':			Instruccions([],'','',[],''),
	   'alma_mater':		Instruccions([],'','',[],''),
	   'tesi':			Instruccions([],'','',[],''),
	   'tesi_any':			Instruccions([],'','',[],''),
	   'direccio_tesi':		Instruccions([],'','',[],''),
	   'conegut_per':		Instruccions([],'','',[],''),
	   'alçada':			Instruccions([],'','',[],''),
	   'pes':			Instruccions([],'','',[],''),
	   'lateralitat':		Instruccions([],'','',[],''),
	   'ulls':			Instruccions([],'','',[],''),
	   'cabells':			Instruccions([],'','',[],''),
	   'camp_treball':		Instruccions([],'','',[],''),
	   'etiqueta_camp_treball':	Instruccions([],'','',[],''),
	   'ocupacio':			Instruccions([],'','',[],''),
	   'etiqueta_ocupacio':		Instruccions([],'','',[],''),
	   'epoca':			Instruccions([],'','',[],''),
	   'etiqueta_epoca':		Instruccions([],'','',[],''),
	   'periode_actiu':		Instruccions([],'','',[],''),
	   'organitzacio':		Instruccions([],'','',[],''),
	   'ocupador':		        Instruccions([],'','',[],''),
	   'mitjans':		        Instruccions([],'','',[],''),
	   'etiqueta_organitzacio':	Instruccions([],'','',[],''),
	   'era':			Instruccions([],'','',[],''),
	   'regio':			Instruccions([],'','',[],''),
	   'escola_tradicio':		Instruccions([],'','',[],''),
	   'interessos':		Instruccions([],'','',[],''),
	   'idees':			Instruccions([],'','',[],''),
	   'opositors':			Instruccions([],'','',[],''),
	   'art':			Instruccions([],'','',[],''),
	   'genere':			Instruccions([],'','',[],''),
	   'moviment':			Instruccions([],'','',[],''),
	   'estil':			Instruccions([],'','',[],''),
	   'mestres':			Instruccions([],'','',[],''),
	   'deixebles':			Instruccions([],'','',[],''),
	   'influencies_de':		Instruccions([],'','',[],''),
	   'influi_en':			Instruccions([],'','',[],''),
	   'llengua':			Instruccions([],'','',[],''),
	   'agent':			Instruccions([],'','',[],''),
	   'editor':			Instruccions([],'','',[],''),
	   'salari':			Instruccions([],'','',[],''),
	   'patrimoni_personal':	Instruccions([],'','',[],''),
	   'lleialtat':			Instruccions([],'','',[],''),
	   'periode_actiu_militar':	Instruccions([],'','',[],''),
	   'arma':			Instruccions([],'','',[],''),
	   'rang':			Instruccions([],'','',[],''),
	   'unitat':			Instruccions([],'','',[],''),
	   'comandaments':		Instruccions([],'','',[],''),
	   'batalles':			Instruccions([],'','',[],''),
	   'victories':			Instruccions([],'','',[],''),
	   'temps_espai':		Instruccions([],'','',[],''),
	   'eva1':			Instruccions([],'','',[],''),
	   'eva2':			Instruccions([],'','',[],''),
	   'tripulacio':		Instruccions([],'','',[],''),
	   'missio_espacial':		Instruccions([],'','',[],''),
	   'insignia_missio':		Instruccions([],'','',[],''),
	   'orde':			Instruccions([],'','',[],''),
	   'ordenacio':			Instruccions([],'','',[],''),
	   'consagracio':		Instruccions([],'','',[],''),
	   'proclamacio':		Instruccions([],'','',[],''),
	   'enaltiment':		Instruccions([],'','',[],''),
	   'data_beatificacio':		Instruccions([],'','',[],''),
	   'lloc_beatificacio':		Instruccions([],'','',[],''),
	   'beatificat_per':		Instruccions([],'','',[],''),
	   'data_canonitzacio':		Instruccions([],'','',[],''),
	   'lloc_canonitzacio':		Instruccions([],'','',[],''),
	   'canonitzat_per':		Instruccions([],'','',[],''),
	   'lloc_pelegrinatge':		Instruccions([],'','',[],''),
	   'venerat_a':			Instruccions([],'','',[],''),
	   'festivitat':		Instruccions([],'','',[],''),
	   'fets destacables':		Instruccions([],'','',[],''),
	   'iconografia':		Instruccions([],'','',[],''),
	   'patronatge':		Instruccions([],'','',[],''),
	   'veu':			Instruccions([],'','',[],''),
	   'instrument':		Instruccions([],'','',[],''),
	   'instruments_destacats':	Instruccions([],'','',[],''),
	   'discografica':		Instruccions([],'','',[],''),
	   'cataleg':			Instruccions([],'','',[],''),
	   'orquestres':		Instruccions([],'','',[],''),
	   'artistes_relacionats':	Instruccions([],'','',[],''),
	   'director_musical':		Instruccions([],'','',[],''),
	   'sotsdirector_musical':	Instruccions([],'','',[],''),
	   'membres':			Instruccions([],'','',[],''),
	   'membres_anteriors':		Instruccions([],'','',[],''),
	   'patrons':			Instruccions([],'','',[],''),
	   'esport':			Instruccions([],'','',[],''),
	   'disciplina':		Instruccions([],'','',[],''),
	   'especialitat':		Instruccions([],'','',[],''),
	   'posicio_equip':		Instruccions([],'','',[],''),
	   'ma_joc':			Instruccions([],'','',[],''),
	   'lliga':			Instruccions([],'','',[],''),
	   'dorsal_club':		Instruccions([],'','',[],''),
	   'draft':			Instruccions([],'','',[],''),
	   'draft_equip':		Instruccions([],'','',[],''),
	   'draft_any':			Instruccions([],'','',[],''),
	   'patrocinador':		Instruccions([],'','',[],''),
	   'lloc_debut':		Instruccions([],'','',[],''),
	   'data_debut':		Instruccions([],'','',[],''),
	   'lloc_retirada':		Instruccions([],'','',[],''),
	   'data_retirada':		Instruccions([],'','',[],''),
	   'entrenador':		Instruccions([],'','',[],''),
	   'equips':	        	Instruccions([],'','',[],''),
	   'participa':			Instruccions([],'','',[],''),
	   'ind_record':		Instruccions([],'','',[],''),
	   'ind_titols':		Instruccions([],'','',[],''),
	   'ind_ranquing_max':		Instruccions([],'','',[],''),
	   'dob_record':		Instruccions([],'','',[],''),
	   'dob_titols':		Instruccions([],'','',[],''),
	   'dob_ranquing_max':		Instruccions([],'','',[],''),
	   'HOF_id':			Instruccions([],'','',[],''),
	   'HOF_any':			Instruccions([],'','',[],''),
	   'atp':			Instruccions([],'','',[],''),
	   'wta':			Instruccions([],'','',[],''),
	   'assessorament_academic':	Instruccions([],'','',[],''),
	   'estudiants_doctorals':	Instruccions([],'','',[],''),
	   'estudiants_notables':	Instruccions([],'','',[],''),
	   'autor_abrev_bot':		Instruccions([],'','',[],''),
	   'autor_abrev_zoo':		Instruccions([],'','',[],''),
	   'obres':			Instruccions([],'','',[],''),
	   'primeres_obres':		Instruccions([],'','',[],''),
	   'programes':			Instruccions([],'','',[],''),
	   'series':			Instruccions([],'','',[],''),
	   'films':			Instruccions([],'','',[],''),
	   'papers':			Instruccions([],'','',[],''),
	   'obres_notables':		Instruccions([],'','',[],''),
	   'principals_projectes':	Instruccions([],'','',[],''),
	   'imatgeobra':		Instruccions([],'','',[],''),
	   'peuobra':			Instruccions([],'','',[],''),
	   'repertori':			Instruccions([],'','',[],''),
	   'trajectoria':		Instruccions(['trajectòria'],'','',[],''),
	   'premis':			Instruccions(['honors'],'','',[],''),
	   'desplega_premis':		Instruccions([],'','',[],''),
	   'monuments':			Instruccions([],'','',[],''),
	   'etiqueta_monuments':	Instruccions([],'','',[],''),
	   'titol_personal':		Instruccions([],'','',[],''),
	   'partit_politic':		Instruccions(['partit_polític'],'','',[],''),
	   'carrecs_judicials':		Instruccions([],'','',[],''),
	   'situacio_judicial':		Instruccions([],'','',[],''),
	   'condemnes':		        Instruccions([],'','',[],''),
	   'dinastia':			Instruccions([],'','',[],''),
	   'etiqueta_dinastia':		Instruccions([],'','',[],''),
	   'conjuge':			Instruccions([],'','',[],''),
	   'parella':			Instruccions([],'','',[],''),
	   'fills':			Instruccions([],'','',[],''),
	   'pares':			Instruccions([],'','',[],''),
	   'pare':			Instruccions([],'','',[],''),
	   'mare':			Instruccions([],'','',[],''),
	   'germans':			Instruccions([],'','',[],''),
	   'parents':			Instruccions([],'','',[],''),
	   'carrec':			Instruccions([],'','',[],''),
	   'escut_carrec':		Instruccions([],'','',[],''),
	   'inici':			Instruccions([],'','',[],''),
	   'final':			Instruccions([],'','',[],''),
	   'predecessor':		Instruccions([],'','',[],''),
	   'successor':			Instruccions([],'','',[],''),
	   'k_etiqueta':		Instruccions(['k-etiqueta'],'','',[],''),
	   'k_nom':		        Instruccions(['k-nom'],'','',[],''),
	   'carrec2':			Instruccions([],'','',[],''),
	   'escut_carrec2':		Instruccions([],'','',[],''),
	   'inici2':			Instruccions([],'','',[],''),
	   'final2':			Instruccions([],'','',[],''),
	   'predecessor2':		Instruccions([],'','',[],''),
	   'successor2':		Instruccions([],'','',[],''),
	   'k_etiqueta2':		Instruccions(['k-etiqueta2'],'','',[],''),
	   'k_nom2':		        Instruccions(['k-nom2'],'','',[],''),
	   'carrec3':			Instruccions([],'','',[],''),
	   'escut_carrec3':		Instruccions([],'','',[],''),
	   'inici3':			Instruccions([],'','',[],''),
	   'final3':			Instruccions([],'','',[],''),
	   'predecessor3':		Instruccions([],'','',[],''),
	   'successor3':		Instruccions([],'','',[],''),
	   'k_etiqueta3':		Instruccions(['k-etiqueta3'],'','',[],''),
	   'k_nom3':		        Instruccions(['k-nom3'],'','',[],''),
	   'escutpeu':			Instruccions([],'','',[],''),
	   'lema_escut':		Instruccions([],'','',[],''),
	   'signatura':			Instruccions([],'','',[],''),
	   'alt_signatura':		Instruccions([],'','',[],''),
	   'registre_veu':		Instruccions([],'','',[],''),
	   'peu_veu':		        Instruccions([],'','',[],''),
	   'lloc_web':			Instruccions([],'','',[],''),
	   'dades_medaller':		Instruccions([],'','',[],''),
	   'notes':			Instruccions([],'','',[],''),
	   'item':			Instruccions([],'','',[],''),
	  }

  a_eliminar = {    # paràmetres que s'esborraran incondicionalment, encara que continguin informació
     'mida_imatge',
     'image_width',
     'imga_width',
     'image1_width',
     'iamge_width'
  }

  def __init__(self):
    self.plant = Xlate.plant
    self.dicci = {}
    for i in list(self.params.keys()):
       #a = self.params[i].p
       #print "llegim ",a
       for elt in self.params[i].vells:
          self.dicci[elt] = i

  def p_associada(self,nom_par):
    try:
       instr = self.params[nom_par]
    except KeyError:
       return ""
    return instr.p

  def aprofitar(self,nom_par):
    instr = self.params[nom_par]
    if instr[0]=='S' or instr[0]=='s':
       return true
    return false

  def tipus_associat(self,nom_par):
    try:
       instr = self.params[nom_par]
    except KeyError:
       return ""
    return instr.tipus

  def plantilles(self):
    return self.plant

  def instruccions (self,plant_orig):
      #Les instruccions estan en una llista d'un sol membre, no té massa sentit
      #de moment
    try:
      instruccions = self.plantilles()[plant_orig][0]
    except:
      print(("*********** No tenim instruccions per plantilla *****",plant_orig))
      return []
    return instruccions

  def cal_esborrar_params(self,plant_orig):
    lletra = self.instruccions(plant_orig)[0]
    if lletra == 'S':
       return True
    else:
       return False

  def nom_objectiu(self):
    return self.nom_final

  def eliminar(self,text):
    if text in self.a_eliminar:
        return True
    else:
        return False

  def traduir(self,text):
    try:
       return self.dicci[text]
    except:
       return text
        

#print params['poblacio'].comment

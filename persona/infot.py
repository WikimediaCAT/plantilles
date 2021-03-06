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
	   'nom':			Instruccions(['Name','name','nomdeljugador','playername','Nom'],'','',[],""),
	   'prefix_honorific':		Instruccions([],'','',[],''),
	   'sufix_honorific':		Instruccions([],'','',[],''),
	   'imatge':			Instruccions(['image','Imatge','Img'],'','',[],''),
	   'peu':			Instruccions(['peu_d\'imatge','caption','image_caption','llegenda','nom imatge'],'','',[],''),
	   'alt':			Instruccions([],'','',[],''),
	   'nom_original':		Instruccions([],'','',[],''),
	   'nom_original_lleng':	Instruccions(['llengua_nom_original'],'','',[],''),
	   'nom_temple':		Instruccions([],'','',[],''),
	   'nom_postum':		Instruccions([],'','',[],''),
	   'nom_naixement':		Instruccions(['fullname','nomreal','nomcomplet','Nom complet'],'','',[],''),
	   'lloc_naixement':		Instruccions(['birth_place'],'','',[],''),
	   'data_naixement':		Instruccions(['birth','datadenaixement','dateofbirth','birth_date','data_naixença','Data de naixement','data_naix','naixement_data','data naixement'],'','',[],''),
	   'bateig':			Instruccions([],'','',[],''),
	   'floruit':			Instruccions([],'','',[],''),
	   'lloc_defuncio':		Instruccions([],'','',[],''),
	   'data_defuncio':		Instruccions(['datademort','dateofdeath','deathdate','death_date','data_defunció','Data de defunció','data_mort','mort_data'],'','',[],''),
	   'causa_defuncio':		Instruccions(['causa_mort','mort_motiu'],'','',[],''),
	   'descobriment_cos':		Instruccions([],'','',[],''),
	   'data_desaparicio':		Instruccions([],'','',[],''),
	   'sepultura':			Instruccions([],'','',[],''),
	   'coordenades_sepultura':	Instruccions([],'','',[],''),
	   'residencia':		Instruccions(['residència','resident'],'','',[],''),
	   'nacionalitat':		Instruccions(['nationality','país','País','pais'],'','',[],''),
	   'ciutadania':		Instruccions([],'','',[],''),
	   'altres noms':		Instruccions([],'','',[],''),
	   'alies':			Instruccions(['sobrenom','nickname','Sobrenom'],'','',[],''),
	   'nom_ploma':			Instruccions([],'','',[],''),
	   'etnia':			Instruccions([],'','',[],''),
	   'ideologia':			Instruccions([],'','',[],''),
	   'religio':			Instruccions(['religió'],'','',[],''),
	   'educacio':			Instruccions([],'','',[],''),
	   'alma_mater':		Instruccions([],'','',[],''),
	   'tesi':			Instruccions([],'','',[],''),
	   'tesi_url':			Instruccions([],'','',[],''),
	   'tesi_any':			Instruccions([],'','',[],''),
	   'tematica':			Instruccions([],'','',[],''),
	   'direccio_tesi':		Instruccions([],'','',[],''),
	   'conegut_per':		Instruccions(['records'],'','',[],''),
	   'alçada':			Instruccions(['height','Alçada'],'','',[],''),
	   'pes':			Instruccions(['weight','Pes'],'','',[],''),
	   'lateralitat':		Instruccions(['braç','dretà-esquerrà'],'','',[],''),
	   'ulls':			Instruccions([],'','',[],''),
	   'cabells':			Instruccions([],'','',[],''),
	   'camp_treball':		Instruccions([],'','',[],''),
	   'etiqueta_camp_treball':	Instruccions([],'','',[],''),
	   'ocupacio':			Instruccions(['actual'],'','',[],''),
	   'etiqueta_ocupacio':		Instruccions([],'','',[],''),
	   'epoca':			Instruccions([],'','',[],''),
	   'etiqueta_epoca':		Instruccions([],'','',[],''),
	   'periode_actiu':		Instruccions([],'','',[],''),
	   'organitzacio':		Instruccions(['negocis'],'','',[],''),
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
	   'patrimoni_personal':	Instruccions(['valor_net','diners','diners guanyats'],'','',[],''),
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
	   'venerat_a':			Instruccions(['venerat_en'],'','',[],''),
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
	   'disciplina':		Instruccions(['estils','modalitat'],'','',[],''),
	   'especialitat':		Instruccions([],'','',[],''),
	   'posicio_equip':		Instruccions(['posició','position','Tipus'],'','',[],''),
	   'ma_joc':			Instruccions([],'','',[],''),
	   'lliga':			Instruccions(['league','lliga'],'','',[],''),
	   'club_actual':		Instruccions(['clubactual','currentclub','team','Equip actual','club'],'','',[],''),
	   'dorsal_club':		Instruccions(['numeroclub','clubnumber','number','dorsal_club','moto'],'','',[],''),
	   'draft':			Instruccions(['draft_pick'],'','',[],''),
	   'draft_equip':		Instruccions(['draft_team','universitat'],'','',[],''),
	   'draft_any':			Instruccions(['draft_year'],'','',[],''),
	   'patrocinador':		Instruccions(['marques','oficial'],'','',[],''),
	   'lloc_debut':		Instruccions(['cursa_1a','debuttrinquet','debutfrontó'],'','',[],''),
	   'data_debut':		Instruccions(['datadebut'],'','',[],''),
	   'lloc_retirada':		Instruccions([],'','',[],''),
	   'data_retirada':		Instruccions(['retirada','dataretirada'],'','',[],''),
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
	   'obres_notables':		Instruccions(['principals_dissenys','models_creats'],'','',[],''),
	   'principals_projectes':	Instruccions([],'','',[],''),
	   'imatgeobra':		Instruccions([],'','',[],''),
	   'peuobra':			Instruccions([],'','',[],''),
	   'repertori':			Instruccions([],'','',[],''),
	   'trajectoria':		Instruccions(['trajectòria'],'','',[],''),
	   'premis':			Instruccions(['honors','condecoracions'],'','',[],''),
	   'desplega_premis':		Instruccions([],'','',[],''),
	   'monuments':			Instruccions([],'','',[],''),
	   'etiqueta_monuments':	Instruccions([],'','',[],''),
	   'titol_personal':		Instruccions([],'','',[],''),
	   'partit_politic':		Instruccions(['partit_polític'],'','',[],''),
	   'carrecs_judicials':		Instruccions([],'','',[],''),
	   'situacio_judicial':		Instruccions([],'','',[],''),
	   'condemnes':		        Instruccions([],'','',[],''),
	   'dinastia':			Instruccions(['casa_reial'],'','',[],''),
	   'etiqueta_dinastia':		Instruccions([],'','',[],''),
	   'conjuge':			Instruccions([],'','',[],''),
	   'parella':			Instruccions([],'','',[],''),
	   'fills':			Instruccions([],'','',[],''),
	   'pares':			Instruccions([],'','',[],''),
	   'pare':			Instruccions([],'','',[],''),
	   'mare':			Instruccions([],'','',[],''),
	   'germans':			Instruccions([],'','',[],''),
	   'parents':			Instruccions([],'','',[],''),
	   'ordre':			Instruccions([],'','',[],''),
	   'carrec':			Instruccions([],'','',[],''),
	   'escut_carrec':		Instruccions([],'','',[],''),
	   'inici':			Instruccions([],'','',[],''),
	   'final':			Instruccions([],'','',[],''),
	   'predecessor':		Instruccions([],'','',[],''),
	   'successor':			Instruccions([],'','',[],''),
	   'junt_a':			Instruccions([],'','',[],''),
	   'k_etiqueta':		Instruccions(['k-etiqueta'],'','',[],''),
	   'k_nom':		        Instruccions(['k-nom'],'','',[],''),
	   'ordre2':			Instruccions([],'','',[],''),
	   'carrec2':			Instruccions([],'','',[],''),
	   'escut_carrec2':		Instruccions([],'','',[],''),
	   'inici2':			Instruccions([],'','',[],''),
	   'final2':			Instruccions([],'','',[],''),
	   'predecessor2':		Instruccions([],'','',[],''),
	   'successor2':		Instruccions([],'','',[],''),
	   'k_etiqueta2':		Instruccions(['k-etiqueta2'],'','',[],''),
	   'k_nom2':		        Instruccions(['k-nom2'],'','',[],''),
	   'ordre3':			Instruccions([],'','',[],''),
	   'carrec3':			Instruccions([],'','',[],''),
	   'escut_carrec3':		Instruccions([],'','',[],''),
	   'inici3':			Instruccions([],'','',[],''),
	   'final3':			Instruccions([],'','',[],''),
	   'predecessor3':		Instruccions([],'','',[],''),
	   'successor3':		Instruccions([],'','',[],''),
	   'k_etiqueta3':		Instruccions(['k-etiqueta3'],'','',[],''),
	   'k_nom3':		        Instruccions(['k-nom3'],'','',[],''),
	   'ordre4':			Instruccions([],'','',[],''),
	   'carrec4':			Instruccions([],'','',[],''),
	   'escut_carrec4':		Instruccions([],'','',[],''),
	   'inici4':			Instruccions([],'','',[],''),
	   'final4':			Instruccions([],'','',[],''),
	   'predecessor4':		Instruccions([],'','',[],''),
	   'successor4':		Instruccions([],'','',[],''),
	   'k_etiqueta4':		Instruccions(['k-etiqueta4'],'','',[],''),
	   'k_nom4':		        Instruccions(['k-nom4'],'','',[],''),
	   'ordre5':			Instruccions([],'','',[],''),
	   'carrec5':			Instruccions([],'','',[],''),
	   'escut_carrec5':		Instruccions([],'','',[],''),
	   'inici5':			Instruccions([],'','',[],''),
	   'final5':			Instruccions([],'','',[],''),
	   'predecessor5':		Instruccions([],'','',[],''),
	   'successor5':		Instruccions([],'','',[],''),
	   'k_etiqueta5':		Instruccions(['k-etiqueta5'],'','',[],''),
	   'k_nom5':		        Instruccions(['k-nom5'],'','',[],''),
	   'ordre6':			Instruccions([],'','',[],''),
	   'carrec6':			Instruccions([],'','',[],''),
	   'escut_carrec6':		Instruccions([],'','',[],''),
	   'inici6':			Instruccions([],'','',[],''),
	   'final6':			Instruccions([],'','',[],''),
	   'predecessor6':		Instruccions([],'','',[],''),
	   'successor6':		Instruccions([],'','',[],''),
	   'k_etiqueta6':		Instruccions(['k-etiqueta6'],'','',[],''),
	   'k_nom6':		        Instruccions(['k-nom6'],'','',[],''),
	   'ordre7':			Instruccions([],'','',[],''),
	   'carrec7':			Instruccions([],'','',[],''),
	   'escut_carrec7':		Instruccions([],'','',[],''),
	   'inici7':			Instruccions([],'','',[],''),
	   'final7':			Instruccions([],'','',[],''),
	   'predecessor7':		Instruccions([],'','',[],''),
	   'successor7':		Instruccions([],'','',[],''),
	   'k_etiqueta7':		Instruccions(['k-etiqueta7'],'','',[],''),
	   'k_nom7':		        Instruccions(['k-nom7'],'','',[],''),
	   'escutpeu':			Instruccions([],'','',[],''),
	   'lema_escut':		Instruccions([],'','',[],''),
	   'signatura':			Instruccions([],'','',[],''),
	   'alt_signatura':		Instruccions([],'','',[],''),
	   'registre_veu':		Instruccions([],'','',[],''),
	   'peu_veu':		        Instruccions([],'','',[],''),
	   'lloc_web':			Instruccions(['website','lloc web','pàgina web','web'],'','',[],''),
	   'dades_medaller':		Instruccions(['medalles','medaltemplates'],'','',[],''),
	   'altres_ocupacions':		Instruccions([],'','',[],''),
	   'designat':		        Instruccions([],'','',[],''),
	   'designat2':		        Instruccions([],'','',[],''),
	   'designat3':		        Instruccions([],'','',[],''),
	   'designat4':		        Instruccions([],'','',[],''),
	   'designat5':		        Instruccions([],'','',[],''),
	   'designat6':		        Instruccions([],'','',[],''),
	   'designat7':		        Instruccions([],'','',[],''),
	   'nominat':		        Instruccions([],'','',[],''),
	   'nominat2':		        Instruccions([],'','',[],''),
	   'nominat3':		        Instruccions([],'','',[],''),
	   'nominat4':		        Instruccions([],'','',[],''),
	   'nominat5':		        Instruccions([],'','',[],''),
	   'nominat6':		        Instruccions([],'','',[],''),
	   'nominat7':		        Instruccions([],'','',[],''),
	   'gabinet':		        Instruccions([],'','',[],''),
	   'gabinet2':		        Instruccions([],'','',[],''),
	   'gabinet3':		        Instruccions([],'','',[],''),
	   'gabinet4':		        Instruccions([],'','',[],''),
	   'gabinet5':		        Instruccions([],'','',[],''),
	   'gabinet6':		        Instruccions([],'','',[],''),
	   'gabinet7':		        Instruccions([],'','',[],''),
	   'oponents':		        Instruccions([],'','',[],''),
	   'oponents2':		        Instruccions([],'','',[],''),
	   'oponents3':		        Instruccions([],'','',[],''),
	   'oponents4':		        Instruccions([],'','',[],''),
	   'oponents5':		        Instruccions([],'','',[],''),
	   'oponents6':		        Instruccions([],'','',[],''),
	   'oponents7':		        Instruccions([],'','',[],''),
	   'junt_a2':		        Instruccions([],'','',[],''),
	   'junt_a3':		        Instruccions([],'','',[],''),
	   'junt_a4':		        Instruccions([],'','',[],''),
	   'junt_a5':		        Instruccions([],'','',[],''),
	   'junt_a6':		        Instruccions([],'','',[],''),
	   'junt_a7':		        Instruccions([],'','',[],''),
	   'a_etiqueta':	        Instruccions([],'','',[],''),
	   'a_etiqueta2':	        Instruccions([],'','',[],''),
	   'a_etiqueta3':	        Instruccions([],'','',[],''),
	   'a_etiqueta4':	        Instruccions([],'','',[],''),
	   'a_etiqueta5':	        Instruccions([],'','',[],''),
	   'a_etiqueta6':	        Instruccions([],'','',[],''),
	   'a_etiqueta7':	        Instruccions([],'','',[],''),
	   'a_nom':	                Instruccions([],'','',[],''),
	   'a_nom2':	                Instruccions([],'','',[],''),
	   'a_nom3':	                Instruccions([],'','',[],''),
	   'a_nom4':	                Instruccions([],'','',[],''),
           'a_nom5':	                Instruccions([],'','',[],''),
	   'a_nom6':	                Instruccions([],'','',[],''),
	   'a_nom7':	                Instruccions([],'','',[],''),
	   'b_etiqueta':	        Instruccions([],'','',[],''),
	   'b_etiqueta2':	        Instruccions([],'','',[],''),
	   'b_etiqueta3':	        Instruccions([],'','',[],''),
	   'b_etiqueta4':	        Instruccions([],'','',[],''),
	   'b_etiqueta5':	        Instruccions([],'','',[],''),
	   'b_etiqueta6':	        Instruccions([],'','',[],''),
	   'b_etiqueta7':	        Instruccions([],'','',[],''),
	   'b_nom':	                Instruccions([],'','',[],''),
	   'b_nom2':	                Instruccions([],'','',[],''),
	   'b_nom3':	                Instruccions([],'','',[],''),
	   'b_nom4':	                Instruccions([],'','',[],''),
	   'b_nom5':	                Instruccions([],'','',[],''),
	   'b_nom6':	                Instruccions([],'','',[],''),
	   'b_nom7':	                Instruccions([],'','',[],''),
	   'e_etiqueta':	        Instruccions([],'','',[],''),
	   'e_etiqueta2':	        Instruccions([],'','',[],''),
	   'e_etiqueta3':	        Instruccions([],'','',[],''),
	   'e_etiqueta4':	        Instruccions([],'','',[],''),
	   'e_etiqueta5':	        Instruccions([],'','',[],''),
	   'e_etiqueta6':	        Instruccions([],'','',[],''),
	   'e_etiqueta7':	        Instruccions([],'','',[],''),
	   'e_nom':	                Instruccions([],'','',[],''),
	   'e_nom2':	                Instruccions([],'','',[],''),
	   'e_nom3':	                Instruccions([],'','',[],''),
	   'e_nom4':	                Instruccions([],'','',[],''),
	   'e_nom5':	                Instruccions([],'','',[],''),
	   'e_nom6':	                Instruccions([],'','',[],''),
	   'e_nom7':	                Instruccions([],'','',[],''),
	   'f_etiqueta':	        Instruccions([],'','',[],''),
	   'f_etiqueta2':	        Instruccions([],'','',[],''),
	   'f_etiqueta3':	        Instruccions([],'','',[],''),
	   'f_etiqueta4':	        Instruccions([],'','',[],''),
	   'f_etiqueta5':	        Instruccions([],'','',[],''),
	   'f_etiqueta6':	        Instruccions([],'','',[],''),
	   'f_etiqueta7':	        Instruccions([],'','',[],''),
	   'f_nom':	                Instruccions([],'','',[],''),
	   'f_nom2':	                Instruccions([],'','',[],''),
	   'f_nom3':	                Instruccions([],'','',[],''),
	   'f_nom4':	                Instruccions([],'','',[],''),
	   'f_nom5':	                Instruccions([],'','',[],''),
	   'f_nom6':	                Instruccions([],'','',[],''),
	   'f_nom7':	                Instruccions([],'','',[],''),
	   'k_etiqueta':	        Instruccions([],'','',[],''),
	   'k_etiqueta2':	        Instruccions([],'','',[],''),
	   'k_etiqueta3':	        Instruccions([],'','',[],''),
	   'k_etiqueta4':	        Instruccions([],'','',[],''),
	   'k_etiqueta5':	        Instruccions([],'','',[],''),
	   'k_etiqueta6':	        Instruccions([],'','',[],''),
	   'k_etiqueta7':	        Instruccions([],'','',[],''),
	   'k_nom':	                Instruccions([],'','',[],''),
	   'k_nom2':	                Instruccions([],'','',[],''),
	   'k_nom3':	                Instruccions([],'','',[],''),
	   'k_nom4':	                Instruccions([],'','',[],''),
	   'k_nom5':	                Instruccions([],'','',[],''),
	   'k_nom6':	                Instruccions([],'','',[],''),
	   'k_nom7':	                Instruccions([],'','',[],''),
	   'l_etiqueta':	        Instruccions([],'','',[],''),
	   'l_etiqueta2':	        Instruccions([],'','',[],''),
	   'l_etiqueta3':	        Instruccions([],'','',[],''),
	   'l_etiqueta4':	        Instruccions([],'','',[],''),
	   'l_etiqueta5':	        Instruccions([],'','',[],''),
	   'l_etiqueta6':	        Instruccions([],'','',[],''),
	   'l_etiqueta7':	        Instruccions([],'','',[],''),
	   'l_nom':	                Instruccions([],'','',[],''),
	   'l_nom2':	                Instruccions([],'','',[],''),
	   'l_nom3':	                Instruccions([],'','',[],''),
	   'l_nom4':	                Instruccions([],'','',[],''),
	   'l_nom5':	                Instruccions([],'','',[],''),
	   'l_nom6':	                Instruccions([],'','',[],''),
	   'l_nom7':	                Instruccions([],'','',[],''),
	   'notes':			Instruccions(['notes_l_peu','footnotes'],'','',[],''),
	   'horus':			Instruccions([],'','',[],''),
	   'horus2':			Instruccions([],'','',[],''),
	   'horushiero':		Instruccions([],'','',[],''),
	   'horushiero2':		Instruccions([],'','',[],''),
	   'horusprefix':		Instruccions([],'','',[],''),
	   'nomen':			Instruccions([],'','',[],''),
	   'nomen2':			Instruccions([],'','',[],''),
	   'nomenhiero':		Instruccions([],'','',[],''),
	   'nomenhiero2':		Instruccions([],'','',[],''),
	   'prenomen':			Instruccions([],'','',[],''),
	   'prenomen2':			Instruccions([],'','',[],''),
	   'prenomenhiero':		Instruccions([],'','',[],''),
	   'prenomenhiero2':		Instruccions([],'','',[],''),
	   'nebty':			Instruccions([],'','',[],''),
	   'nebtyhiero':		Instruccions([],'','',[],''),
	   'golden':			Instruccions([],'','',[],''),
	   'goldenhiero':		Instruccions([],'','',[],''),
	   'extensio_parametres_esport':Instruccions([],'','',[],''),
	   'extensio_carrera_esportiva':Instruccions([],'','',[],''),
	   'extensio_carrecs_successoris':Instruccions([],'','',[],''),
	   'extensio_participacio_esdeveniments':Instruccions([],'','',[],''),
	   'extensio_guardons':         Instruccions([],'','',[],''),
	   'list_naixement':            Instruccions([],'','',[],''),
	   'item':			Instruccions([],'','',[],''),
	  }

  a_eliminar = {    # paràmetres que s'esborraran incondicionalment, encara que continguin informació
     'mida_imatge',
     'image_width',
     'imga_width',
     'image1_width',
     'iamge_width',
     'supressio_culte',
     'imatge_espiritual',
     'peu_imatge_espiritual',
     'origen',
     'principals_edificis',
     'millors_films',
     'ordre8',
     'carrec8',
     'escut_carrec8',
     'inici8',
     'final8',
     'predecessor8',
     'successor8',
     'k_etiqueta8',
     'k_nom8',    
     'designat8',    
     'nominat8',    
     'govern8',    
     'oponents8',    
     'junt_a8',    
     'a_etiqueta8',
     'a_nom8',
     'b_etiqueta8',
     'b_nom8',
     'e_etiqueta8',
     'e_nom8',
     'f_etiqueta8',
     'f_nom8',
     'k_etiqueta8',
     'k_nom8',
     'l_etiqueta8',
     'l_nom8',
     'ntupdate',
     'equipnacional-update',
     'club-update',
     'pcupdate',
     'totalcaps',
     'totalgoals'
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

class Xlate_esportista(Xlate):
    def __init__(self):
        self.params['clubsjuvenils'] = Instruccions(['youthclubs'],'','',[],'')
        self.params['anysjuvenils'] = Instruccions(['youthyears'],'','',[],'')
        self.params['clubs'] = Instruccions(['teams','Equips anteriors'],'','',[],'')
        self.params['anys'] = Instruccions(['years'],'','',[],'')
        self.params['partits'] = Instruccions(['caps'],'','',[],'')
        self.params['gols'] = Instruccions(['goals'],'','',[],'')
        self.params['equipnacional'] = Instruccions(['seleccio_nacional','nationalteam','selecciónacional'],'','',[],'')
        self.params['anysnacional'] = Instruccions(['nationalyears'],'','',[],'')
        self.params['partitsnacional'] = Instruccions(['nationalcaps'],'','',[],'')
        self.params['golsnacional'] = Instruccions(['nationalgoals'],'','',[],'')
        self.params['clubsentrenats'] = Instruccions(['clubsentrenador','managerclubs','equipsentrenats'],'','',[],'')
        self.params['anysentrenador'] = Instruccions(['anysentrenats','manageryears'],'','',[],'')
        # aquests paràmetres s'esborraran igualment
        self.params['ciutatdenaixement'] = Instruccions(['cityofbirth'],'','',[],'')
        self.params['paisdenaixement'] = Instruccions(['paísdenaixement','countryofbirth'],'','',[],'')
        self.params['ciutatdemort'] = Instruccions(['cityofdeath'],'','',[],'')
        self.params['paisdemort'] = Instruccions(['paísdemort','countryofdeath'],'','',[],'')
        # fi de paràmetres, ara inicialitzem la resta
        Xlate.__init__(self)
        # aquests s'han de fer després, per matxacar el que ha fet
        # l'altre init
        self.plant['Infotaula esportista'] = [('S','','')]
        self.nom_final = "Infotaula esportista"

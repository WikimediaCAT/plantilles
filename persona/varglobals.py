# -*- coding: utf-8 -*-

import codecs
import re
import wdint
import pywikibot

def sel_itemwd(pag):
   wd = wdint.WDint()
   siteca = pywikibot.Site('ca')
   pag = pywikibot.Page(siteca,nom_article)

   itemwd = wd.wd_q_des_de_pag(pag)
   return wd


def treure_brs(string):
    reg=r'<\s*[Bb][Rr]\s*[\/\\]?\s*>\s*'
    string= re.sub(reg,' ',string)
    string= string.replace('\n',' ')
    #print "Després de treure_brs ",string
    return string

def escapa_coses(primer):
    primer = primer.replace("(","\(")
    primer = primer.replace(")","\)")
    primer = primer.replace("[","\[")
    primer = primer.replace("]","\]")
    primer = primer.replace(".","\.")
    primer = primer.replace(" ","[_ ]")
    primer = primer.replace("+","\+")
    primer = primer.replace("*","\*")
    primer = primer.replace("?","\?")
    return primer

# compara dos strings i retorna True si són iguals, False si són diferents
# per comparar, considerem igual el caràcter "_" que " "
def comp_fitx(primer,segon):
    if len(primer)==1:
      if len(segon)==1:
        return (primer.toupper()==segon.toupper())
      else:
        return False
    if len(primer)==0 or len(segon)==0:
        return False
    if primer[0].isalpha():
      alfabet = True
      inicireg=r'['+primer[0].upper()+primer[0].lower()+r']'  # ho fem aquí
                    # per si el nom de fitxer comença amb parèntesis o coses rares
    else:
      alfabet = False
    primer = escapa_coses(primer)
    if alfabet:
      primer = inicireg+primer[1:]
    #print("Anem al match amb \"%s\" i \"%s\"" % (primer, segon))

    return (re.match(primer,segon)!=None)

def init():
  global fout
  global foutimatges
  #global foutrepassarimatges
  global nom_article
  fout = codecs.open('coses_a_revisar','a',encoding='utf-8')
  foutimatges = codecs.open('imatges_a_revisar','a',encoding='utf-8')
  #foutrepassarimatges = codecs.open('articles_amb_imatge','a',encoding='utf-8')
  nom_article = ""

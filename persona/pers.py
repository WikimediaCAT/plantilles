# -*- coding: utf-8 -*-
import pywikibot
import re
import sys
import locale
import codecs
import time

import tipus
import varglobals
#import wdint

from infot import Xlate, Xlate_esportista
from tipus import Text_art, Plantilla, elimina_comment
from pywikibot.version import getversion
from pywikibot.login import LoginManager

fit = codecs.open('entrada','r',encoding='utf-8')
proves = codecs.open('text','r',encoding='utf-8')      #fitxer de proves
                                                    # per no llegir sempre de VP

def preguntar():
  while 1:
   a = input("Canviar? (s/n/t) ")
   #a=sys.stdin.readline()
   a=a.rstrip()
   if a=='t':
       return 0
   if a=='s':
       return 1
   if a=='n':
       return -1

def main():
 locale.setlocale(locale.LC_ALL, '')
 print(sys.version)
 print(getversion())

 varglobals.init()
 #reload(sys)
 #sys.setdefaultencoding('utf-8')
 preguntem=True
 siteca = pywikibot.Site('ca')

 for pagina in fit:

   article=pagina
   article=article.rstrip()
   print(article.encode("utf-8"))

   # per treballar amb fitxer de proves, comentar a partir d'aquí
   pag = pywikibot.Page(siteca,article)
   min = 1
   tornar_amunt = False
   while True:
    try:
      txtorig = pag.get()
      break
    except pywikibot.IsRedirectPage:
      pag     = pag.getRedirectTarget()
      txtorig = pag.get()
      article = pag.title()
      break
    except pywikibot.NoPage:
      tornar_amunt = True
      break
    except pywikibot.data.api.APIError:
      time.sleep(min*60)
      min = min+1
   # si no és de l'espai de noms normal no hi volem entrar
   if pag.namespace() != 0:
      continue
   if tornar_amunt:
      continue
   '''
   # per treballar amb fitxer de proves, comentar fins aquí

   txtorig = proves.read()
   '''

   varglobals.nom_article=article
   #xl = Xlate()
   xl = Xlate_esportista()

   txtnou = txtorig

   t = Text_art(article,txtnou,xl)

   #print u"Tot l'objecte text"
   #print t.__repr__().encode('utf-8')

   t.adapta()
   txtnou = t.genera()

   if txtorig != txtnou:
     try:
        pywikibot.showDiff(txtorig,txtnou)
        comentari = "Robot normalitza infotaula persona"

	# per treballar amb fitxer de proves, comentar a partir d'aquí
        if preguntem :
           quefem=preguntar()
           #quefem = -1
           if quefem==0 :
              preguntem=False
           if quefem == 1 or quefem == 0:
              print("Gravant")
              pag.put(txtnou,summary=comentari,minor=False)
              pass
              #return 0
           else:
              pass           # no fem res
              #exit(-1)
        else:
          min = 1
          while True:
            try:
              pag.put(txtnou,summary=comentari,minor=False)
              pass
              break
            except (pywikibot.exceptions.OtherPageSaveError, pywikibot.data.api.APIError):
              print("******************** Error de salvat, esperem ********************")
              time.sleep(min*60)
              min = min + 1
	# per treballar amb fitxer de proves, comentar fins d'aquí

     except KeyboardInterrupt:
        return
        pass

 varglobals.fout.write("|}")
 varglobals.fout.close()
 varglobals.foutimatges.write("|}")
 varglobals.foutimatges.close()

if __name__ == '__main__':
    try:
        main()
    finally:
        pywikibot.stopme()

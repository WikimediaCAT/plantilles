# -*- coding: utf-8 -*-
import pywikibot
import pprint
import time

import varglobals

class WDint:
    """ Interfície amb wikidata                     """
    """ wdsite: Site de wikidata                    """
    """ repowd: repositori                          """
    """ item:   item seleccionat                    """

    def llegir_fitxer(self,target):
        print(("Fitxer wikidata: "+target.title(with_ns=False)))

    def llegir_quantitat(self,target):
        print(("Quantitat: ",target.amount))

    def llegir_string(self,target):
        print(target)

    def llegir_p_wd(self,p):
       pp = pprint.PrettyPrinter(indent=4)

       if self.item == None:
           print("******* Error, item no seleccionat *********")
           return
       #print("Mirem propietat %s" % p)
       if p=="":
          return None

       if p in self.item.claims:    # si hi ha la propietat a wikidata
           clm_dict = self.item.claims
           clm_estat = clm_dict[p]    # això és tot el paquet de valors
           for elt in clm_estat:
               val = elt.getTarget()
               return val
       else:
           return None

    def act_wd_audio_peu(self,fitxer,peu):
       if self.item == None:
           print("Error, item no seleccionat")
           return
       print("********** ATENCIO Posant àudio a Wikidata **************************")
       nouclm = pywikibot.Claim(self.repowd,'P51')
       nouclm.setTarget(fitxer)
       importatde = pywikibot.Claim(self.repowd,'P143')
       importatde.setTarget(pywikibot.ItemPage(self.repowd,'Q199693'))
       # importat de viquipèdia en català
       lrefs=[importatde]
       self.item.addClaim(nouclm)
       nouclm.addSources(lrefs)
       if peu.strip()!="":
         qualif = pywikibot.Claim(self.repowd,'P2096')
         qualif.setTarget(pywikibot.WbMonolingualText(text=peu,language='ca'))
         nouclm.addQualifier(qualif)

    # Actualitza una imatge a Wikidata
    def act_wd_imatge_peu(self,fitxer,peu):
       if self.item == None:
           print("Error, item no seleccionat")
           return
       print("Posant imatge a Wikidata")
       nouclm = pywikibot.Claim(self.repowd,'P18')
       nouclm.setTarget(fitxer)
       importatde = pywikibot.Claim(self.repowd,'P143')
       importatde.setTarget(pywikibot.ItemPage(self.repowd,'Q199693'))
       # importat de viquipèdia en català
       lrefs=[importatde]
       self.item.addClaim(nouclm)
       nouclm.addSources(lrefs)
       if peu.strip()!="":
         qualif = pywikibot.Claim(self.repowd,'P2096')
         qualif.setTarget(pywikibot.WbMonolingualText(text=peu,language='ca'))
         minuts = 1
         # Wikidata dóna molts timeouts, hem de posar més controls
         while True:
           try:
              nouclm.addQualifier(qualif)
              break
           except pywikibot.exceptions.MaxlagTimeoutError:
              time.sleep(minuts*120)
              minuts = minuts + 1
              nouclm.addQualifier(qualif)

    # actualitza el peu d'imatge en català d'una imatge donada a Wikidata
    def act_wd_peu(self,fitxer,peu,propietat):
       if len(peu)==0:
           return
       if self.item == None:
           print("Error, item no seleccionat")
           return
       #print self.item_dict
       if propietat in self.item.claims:    # si hi ha imatge a wikidata
           clm_dict = self.item_dict["claims"]
           clm_fitxer = clm_dict[propietat]     # això és tot el paquet d'imatges
           for clm in clm_fitxer:           # pot haver-hi més d'una imatge
               tg = clm.getTarget()
               #print tg
               #print type(tg)
               #print dir(tg)
               nom_fitxer = tg.title(with_ns=False)
               if varglobals.comp_fitx(nom_fitxer,fitxer):    # aquest és el fitxer on hem de
                                           # posar el peu de foto
                  print("Posant peu d'imatge a Wikidata")
                  qualif = pywikibot.Claim(self.repowd,'P2096')
                  qualif.setTarget(pywikibot.WbMonolingualText(text=peu,language='ca'))
                  clm.addQualifier(qualif)
       
    # retorna una llista de tuples amb les imatges i el peu d'imatge a Wikidata
    def imatge_i_peu(self,propietat):
       nom_fitxer = peu_imatge = ""
       resultat = []
       if self.item == None:
           print("Error, item no seleccionat")
           return
       #print self.item_dict
       if propietat in self.item.claims:    # si hi ha imatge a wikidata
           clm_dict = self.item_dict["claims"]
           clm_fitxer = clm_dict[propietat]     # això és tot el paquet d'imatges
           for clm in clm_fitxer:           # pot haver-hi més d'una imatge
               tg = clm.getTarget()
               #print tg
               #print type(tg)
               #print dir(tg)
               nom_fitxer = tg.title(with_ns=False)
               try:
                 wdqual = clm.qualifiers['P2096']   # mirem si hi ha llegenda
                 for peusimatge in wdqual:      # pot estar en molts idiomes
                    textqual = peusimatge.getTarget()
                    #print type(textqual)
                    #print dir(textqual)
                    if textqual.language=='ca':
                      peu_imatge = textqual.text
               except KeyError:         # no hi ha P2096
                 peu = ""
               # hem trobat una imatge amb peu, l'afegim
               if clm.getRank() == "preferred":
                  # si és preferred, la posem al principi
                  resultat.insert(0,(nom_fitxer,peu_imatge))
               else:
                  # si no, a la cua
                  resultat.append((nom_fitxer,peu_imatge))
       return resultat
                 
    def get_item(self):
       return self.item

    def get_id(self):
        if self.item == None:
            return None
        return self.item.getID()

    def wd_q_des_de_pag(self,pagina):
       minuts = 1
       try:
           self.item = pywikibot.ItemPage.fromPage(pagina,self.wdsite)
       except pywikibot.exceptions.NoPage:
           print("Article ",pagina.title()," sense wikidata")
           return None
       # la comprovació anterior sembla que no funciona
       # si no existeix a Wikidata. Però si llavors intentes utilitzar
       # self.item, peta. Per tant, ho provem
       try:
           if self.item == -1:
               print("Això no ha de passar mai, perquè donarà excepció")
       except pywikibot.exceptions.NoPage:
           print("Article "+pagina.title()+" sense wikidata")
           return None

       # Wikidata dóna molts timeouts, hem de posar més controls
       while True:
           try:
              self.item_dict = self.item.get()
              break
           except pywikibot.exceptions.MaxlagTimeoutError:
              time.sleep(minuts*120)
              minuts = minuts + 1
              self.item_dict = self.item.get()

       return self.item

    def __str__(self):
       return self.item
    def __init__(self):
       self.wdsite = pywikibot.Site("wikidata", "wikidata")
       self.repowd = self.wdsite.data_repository()
       self.item = None

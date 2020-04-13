# -*- coding: utf-8 -*-
import re
import operator
import pywikibot
import wdint

import varglobals

from collections import namedtuple
import pprint


def hiharef(text):
    mo = re.search(
        r"<[Rr][Ee][Ff]\s*[Nn][Aa][Mm][Ee](.*?)<\/[Rr][Ee][Ff]>",
        text)
    if mo is not None:
        return len(mo.group(1))
    else:
        return 0


def separar_refsambnom(string):
    refsencera = r".*?(<[Rr][Ee][Ff](\s*name\s*=[^>]*)?\s*>.*<\s*/[Rr][Ee][Ff]\s*>)"
    llista = []
    for m in re.finditer(refsencera, string):
        # separem la referencia trobada, i la passem a la llista i la traiem
        # del contingut
        llista.append(m.group(1))
    return llista


def separar_refs(string):
    refsencera = r".*?(<[Rr][Ee][Ff](\s*name\s*=[^>]*)?\s*>.*<\s*/[Rr][Ee][Ff]\s*>)"
    refaref = r".*?(<[Rr][Ee][Ff](\s*name\s*=[^>]*)?\s*\/\s*>)"
    llista = []
    contingut = string
    for m in re.finditer(refsencera, string):
        # separem la referencia trobada, i la passem a la llista i la traiem
        # del contingut
        llista.append(m.group(1))
        contingut = contingut[:m.start(1)] + contingut[m.end(1):]
    for m in re.finditer(refaref, string):
        llista.append(m.group(1))
        contingut = contingut[:m.start(1)] + contingut[m.end(1):]

    return (contingut.strip(), llista)


def treu_comentari(string):
    regex = r"<!--.*?-->"
    str = re.sub(regex, r"", string)
    return str

# Retorna False si hi ha alguna cosa xunga que no es pugui arreglar automàticament
# dins de l'string


def detecta_barres(string):
    mo = re.search(r"\[\[\s*(Fitxer|File)\s*:", string)
    if mo is not None:
        print(
            "*************** ATENCIO: Fitxer dins de l'string   *************************")
        return False
    claud = 0
    for l in string:
        if l == '[' or l == '{':
            claud = claud + 1
        elif l == ']' or l == '}':
            claud = claud - 1
        elif l == '|':
            if claud != 2:
                print(
                    "*************** ATENCIO: Barra (|) fora de claudàtors **********************")
                return False
    if claud != 0:
        print(
            "*************** ATENCIO: Claudàtors desequilibrats  ************************")
        return False
    return True

# Treu la wikisintaxi d'un string


def treure_markup(string):

    # és important l'ordre. Primer la regex més específica
    regmida2 = r"{{mida\s*\|\s*[0-9]+%\s*\|(.*?)}}"
    regmida = r"{{mida\s*\|\s*1?=?(.*?)}}"
    str2 = re.sub(regmida2, r"\1", string)
    str2 = re.sub(regmida, r"\1", str2)

    (str2, ljunk) = separar_refs(str2)
    if not detecta_barres(str2):
        print(("Error en article " + varglobals.nom_article))
        return string
    regcometes = r"('{2,3})(.*?)\1"
    regclaudambbarra = r"\[\[[^]]+?\|([^]]+?)\]\]"
    regclaudsensebarra = r"\[\[([^]]*?)\]\]"
    regtags = r"<\s*[ibIB]\s*>(.*?)<\s*\/[ibIB]\s*>"
    regapostrof = r"{{'}}"
    regnbsp = r"&nbsp;"
    reghtml = r"&[a-z0-9]+;"

    str2 = re.sub(regtags, r"\1", str2)
    str2 = re.sub(regcometes, r"\2", str2)
    str2 = re.sub(regcometes, r"\2", str2)
    #print "primera", str2
    str2 = re.sub(regclaudambbarra, r"\1", str2)
    #print "segona", str2
    str2 = re.sub(regclaudsensebarra, r"\1", str2)
    #print "tercera", str2
    str2 = re.sub(regapostrof, "'", str2)
    str2 = re.sub(regnbsp, " ", str2)
    str2 = varglobals.treure_brs(str2)
    str2 = str2.strip()
    # plantilla Taxon
    regtaxon = r"{{[Tt]àxon\s*\|([^|]*)\|([^|]*)\|([^}]*)}}"
    (str2, nsubs) = re.subn(regtaxon, r"\1. \3", str2)
    if nsubs > 0:
        print(
            "******************ATENCIO: Substitució de Tàxon   **************************")

    if re.search(reghtml, str2) is not None:
        print(
            "*************** ATENCIO: Entitats HTML a l'string  *************************")
        print(("Error en article " + varglobals.nom_article))
    if re.search(r"{{|}}", str2) is not None:
        print("*************** ATENCIO: Plantilla a l'string     *************************")
        print(("Error en article " + varglobals.nom_article))
    return str2


def fitxer_es_audio(nomfit):
    reg = r".*\.(.+)"
    mo = re.match(reg, nomfit)
    if mo is None:
        return False
    extensio = mo.group(1).lower()

    if extensio == "ogg" or extensio == "wav" or extensio == "oga":
        return True
    return False


def fitxer_es_imatge(nomfit):
    reg = r".*\.(.+)"
    mo = re.match(reg, nomfit)
    if mo is None:
        return False
    extensio = mo.group(1).lower()

    if extensio == "jpg" or extensio == "jpeg" or extensio == "gif" \
            or extensio == "png" or extensio == "tif" \
            or extensio == "svg":
        return True
    return False


def elimina_comment(text):
    encoment = False
    ret = ""
    i = 0
    while i < len(text):
        if text[i:i + 4] == '<!--':
            encoment = True
            i = i + 4
        if encoment and text[i:i + 3] == '-->':
            encoment = False
            i = i + 3
        if not encoment and i < len(text):
            ret = ret + text[i]
        i = i + 1
    return ret.strip()


def cau_en_un_forat(forats, num):
    r = 0
    #print forats
    while r < len(forats):
        if forats[r][0] < num and num < forats[r][1]:
            return True
        r = r + 1
    return False


Trio_plant = namedtuple('Trio_plant', ['plantilla', 'inici', 'final'])


class Parametre:
    """ Descripció d'un paràmetre de la plantilla				"""
    """ Variables:							"""
    """ nom_par: nom del paràmetre					"""
    """ igual: booleà, si conté igual o no				"""
    """ val_par: valor del paràmetre					"""

    def tanquemref(self, text):
        tancaref = re.compile(r"<\s*/[Rr][Ee][Ff]\s*>")
        mo = tancaref.match(text)
        if mo is not None:
            return (True, mo.end())
        else:
            return (False, 0)

    def obrimref(self, text):

        obriref = re.compile(r"<\s*[Rr][Ee][Ff].*?>")
        tancada = re.compile(r"<\s*[Rr][Ee][Ff].*?\/\s*>")

        mo = obriref.match(text)
        if mo is not None:
            # encara pot ser del tipus <ref name="xxx"/>
            if tancada.match(text) is None:
                return (True, mo.end())
            else:
                return (False, 0)
        return (False, 0)

    def trobar_str_par(self, text, cond_fi):
        i = 0
        encomentari = False
        enref = False
        depth = 0

        while i < len(text):
            if encomentari and text[i:i + 3] == "-->":
                i = i + 3
                encomentari = False
                if i < len(text):
                    continue
                else:
                    break

            if text[i:i + 4] == "<!--":
                encomentari = True
                i = i + 4
                if i < len(text):
                    continue
                else:
                    break
            if enref:
                estanca, salt = self.tanquemref(text[i:])
                if estanca:
                    enref = False
                    i = i + salt
                    continue
            else:
                sobre, salt = self.obrimref(text[i:])
                if sobre:
                    enref = True
                    i = i + salt
                    continue
            if text[i:i + 2] == "{{" or text[i:i + 2] == "[[":
                depth = depth + 1
                i = i + 2
                if i < len(text):
                    continue
                else:
                    break

            if text[i:i + 2] == "}}" or text[i:i + 2] == "]]":
                depth = depth - 1
                i = i + 2
                if i < len(text):
                    continue
                else:
                    i = i - 2  # hem trobat el tancament de la plantilla
                    break

            if text[i] in cond_fi and depth == 0 and not enref and not encomentari:
                #print u"sortim de trobar_str_par",text[0:i],u"i és",i
                return i
            i = i + 1
        return i

    def te_igual(self):
        return self.igual

    def nom_param(self):
        return self.nom_par

    def set_valor(self, valor):
        self.val_par = valor
        return

    def valor_param(self):
        return self.val_par

    def mida(self):
        return self.llargada

    def __init__(self, text, nom=None, signeigual=None, valor=None):
        # Aquest constructor té trampa. Es pot cridar amb un text i prou
        # o amb un text qualsevol (en principi, en blanc) i els tres paràmetres
        # amb nom. Si els paràmetres estan informats, es crea per còpia
        # si no, es crea escanejant el text
        if nom is not None and signeigual is not None and valor is not None:
            self.nom_par = nom
            self.igual = signeigual
            self.val_par = valor
            return
        self.igual = False
        self.nom_par = ""
        self.val_par = ""
        self.llargada = 0
        ind = self.trobar_str_par(text, "=|}")
        if ind == 0:  # si no hem trobat igual, ja ho tenim
            return
        parametre = text[0:ind].strip()
        if len(parametre) == 0:  # parametre buit, pleguem
            return
        if text[ind] == "=":
            self.igual = True
        elif text[ind] == "|" or text[ind] == "}":
            self.igual = False
        else:
            print((
                "******* Situació estranya buscant nom de paràmetre",
                parametre,
                " ***************"))
        self.nom_par = parametre

        if ind < len(text):
            ind = ind + 1
        if self.igual:
            ind2 = self.trobar_str_par(text[ind:], "|}")
            self.val_par = text[ind:ind + ind2].strip()
            self.llargada = ind + ind2
        #print u"paràmetre",self.nom_par, u"valor",self.val_par

        return

    def __repr__(self):
        return ("Paràmetre %s, valor %s" % (self.nom_par,self.val_par))


class Text_art:
    """ Text_art, amb operacions bàsiques per tractar el text de          """
    """ l'article								"""
    """ Variables:							"""
    """ cursor: per on anem llegint					"""
    """ comments: taula de llocs del text comentats			"""
    """ plantilles: taula amb les plantilles que conté el text		"""

    def taula_comments(self, text):
        taula = []
        encomentari = False
        i = 0
        while True:
            if encomentari and text[i:i + 3] == "-->":
                i = i + 3
                encomentari = False
                taula.append((inicoment, i))
                if i < len(text):
                    continue
                else:
                    break
            if text[i:i + 4] == "<!--":
                encomentari = True
                inicoment = i
                i = i + 4
                if i < len(text):
                    continue
                else:
                    break
            i = i + 1
            if i < len(text):
                continue
            else:
                break
        return taula

    def cau_en_plantilles(self, index):
        for elt in self.plantilles:
            if index > elt.inici and index < elt.final:
                print(
                    "**************************** ATENCIO possible destrossa en plantilla *********************************")

    def mira_recupera_refs(self, llista):
        noustring = self.text
        for ref in llista:
            for l in ref:
                mo = re.search(
                    r"<[Rr][Ee][Ff]\s*[Nn][Aa][Mm][Ee]\s*=\s*\"?(.*?)\"?\s*>(.*?)<\/[Rr][Ee][Ff]>",
                    l)
                if mo is not None:
                    matchtot = mo.group(0)
                    nomrefer = mo.group(1)
                    regnova = r"<[Rr][Ee][Ff]\s*[Nn][Aa][Mm][Ee]\s*=\s*\"?" + \
                        nomrefer + r"\"?\s*\/\s*>"
                    regnova_alt = r"<[Rr][Ee][Ff]\s*[Nn][Aa][Mm][Ee]\s*=\s*\"?" + \
                        nomrefer + r"\"?\s*><\s*\/\s*[Rr][Ee][Ff]\s*>"
                    mo = re.search(regnova, noustring)
                    if mo is not None:
                        self.cau_en_plantilles(mo.start(0))

    def recupera_refs(self, textfinal, llista):
        noustring = textfinal
        for ref in llista:
            for l in ref:
                print("recuperant ", l)
                mo = re.search(
                    r"<[Rr][Ee][Ff]\s*[Nn][Aa][Mm][Ee]\s*=\s*\"?(.*?)\"?\s*>(.*?)<\/[Rr][Ee][Ff]>",
                    l)
                if mo is not None:
                    matchtot = mo.group(0)
                    nomrefer = mo.group(1)
                    print(
                        "buscarem ref",
                        mo.group(1),
                        "i la posarem per ",
                        matchtot)
                    regnova = r"<[Rr][Ee][Ff]\s*[Nn][Aa][Mm][Ee]\s*=\s*\"?" + \
                        nomrefer + r"\"?\s*\/\s*>"
                    regnova_alt = r"<[Rr][Ee][Ff]\s*[Nn][Aa][Mm][Ee]\s*=\s*\"?" + \
                        nomrefer + r"\"?\s*><\s*\/\s*[Rr][Ee][Ff]\s*>"
                    mo = re.search(regnova, noustring)
                    noustring = re.sub(regnova, matchtot, noustring, 1)
                    if noustring != textfinal:  # s'ha fet un canvi
                        print(
                            "********************* afegint referència format curt *********************")
                    else:                 # no s'ha fet el canvi, provem una altra regex
                        noustring = re.sub(regnova_alt, matchtot, noustring, 1)
                        if noustring != textfinal:
                            print(
                                "********************* afegint referència format llarg *********************")
        return noustring


    def trobar_plantilles(self, xl):
        self.plantilles = []
        set_plantilles = xl.plantilles()
        for i in list(set_plantilles.keys()):
                #print u"Buscant plantilla **"+i+"***"
            strreg_i = r'[' + i[0].upper() + i[0].lower() + r']' + i[1:]
            # per si hi ha doble espai
            strreg_i = strreg_i.replace("\u00a0"," ")
            strreg_i = re.sub(' ', r'[ _]+', strreg_i)
            reg = r'{{\s*(Plantilla\s*:\s*)?' + strreg_i + r"(\s*[<}|])"
            ind = 0
            while True:
                mo = re.search(reg, self.text[ind:], re.DOTALL)
                if mo is None:
                    break
                inici = mo.start()
                #print mo.group(),ind,mo.start()
                if cau_en_un_forat(
                        self.comments, ind + inici):  # està comentat
                    #print "cau en un forat"
                    ind = ind + mo.end()
                    continue
                #print u"Creant plantilla de nom ",i,u"en posició",inici+ind
                p_nova = Plantilla(self.text[inici + ind:], i, xl)
                mida = p_nova.mida()
                nou_elt = Trio_plant(
                    plantilla=p_nova,
                    inici=inici + ind,
                    final=inici + ind + mida)
                #nou_elt = (p_nova,inici+ind,inici+mida)
                ind = ind + mo.end()
                self.plantilles.append(nou_elt)
        if len(self.plantilles) == 0:
            print("**************** ULL - No hi ha plantilla ***************")
        return
        print("Trobades totes les plantilles")
        for i in self.plantilles:
            print((i.inici, i.final))
            print((type(i.plantilla)))
            print((i[0].__repr__().encode('utf-8')))
        print("Fi totes les plantilles trobades")

    def adapta(self):
        lrefs = []
        #print("som a adapta")
        for p in self.plantilles:
            if p.plantilla.titol in self.xl.plantilles(
            ) or p.plantilla.titol == self.xl.nom_objectiu():
                #print "Hem trobat plantilla a traduir"
                #print self.xl.nom_objectiu()
                if self.xl.cal_esborrar_params(p.plantilla.titol):
                    p.plantilla.titol = self.xl.nom_objectiu()
                    # p.plantilla.preproces()
                    p.plantilla.traduit()
                    p.plantilla.tractar_wikidata(self.nom_article)
                    #p.plantila.mirar_peus_sense_imatge()
                    # p.plantilla.aval_wd(wd)
                else:
                    print("********* Plantilla que no sabem què fer")
        return

    def nom_par(self, nom_abuscar):
        for p in self.plantilles:
            return p.plantilla.get_par(nom_abuscar)

    def genera(self):
        ordenades = sorted(self.plantilles, key=operator.attrgetter('inici'))
        cursor = 0
        toret = ""
        for i in ordenades:
            toret = toret + self.text[cursor:i.inici]
            # ens assegurem que la plantilla comenci línia
            if (i.inici > 0) and self.text[i.inici - 1] != '\n':
                toret = toret + '\n'
            toret = toret + i.plantilla.pintar()
            cursor = i.final
            self.lrefs.extend(i.plantilla.referenciesesborrades())
        # això ho fem perquè després de la plantilla hi hagi un salt de línia
        # primer mirem si hi ha espais en blanc després de la plantilla
        while self.text[cursor].isspace() and self.text[cursor]!='\n':
            cursor += 1
        # si hem sortit perquè no hi ha espai en blanc, inserim salt de línia
        if self.text[cursor]!='\n':
           toret = toret + '\n'
        # agafem la resta del text
        toret = toret + self.text[cursor:]
        # si hem esborrat referències les recuperem
        toret = self.recupera_refs(toret, self.lrefs)
        return toret

    def textet(self):
        return self.text

    def __repr__(self):
        repre = self.text + "\nComentaris:"
        comme = ""
        for i in self.comments:
            comme = comme + '%d,%d\n' % (i[0], i[1])
        plant = "\nPlantilles:"
        for i in self.plantilles:
            plant = plant + i[0].__repr__()
        return repre + comme + plant

    def __init__(self, nom_art, txt, xl):
        self.text = txt
        self.comments = self.taula_comments(txt)
        self.trobar_plantilles(xl)
        self.xl = xl
        self.nom_article = nom_art
        self.lrefs = []


class Plantilla:
    """ Plantilla, amb les operacions bàsiques per manipular-la		"""
    """ Variables:							"""
    """ titol: l'identificador de la plantilla				"""
    """ text: el text de la plantilla 					"""
    """ forats: té controlats el que no són paràmetres substituibles	"""

    def recalcular_forats(self, textet):
        encomentari = False
        self.forats = []
        depth = i = 0
        while True:
            if encomentari and textet[i:i + 3] == "-->":
                i = i + 3
                encomentari = False
                if i < len(textet):
                    continue
                else:
                    break
            if textet[i:i + 4] == "<!--":
                i = i + 4
                encomentari = True
                if i < len(textet):
                    continue
                else:
                    break
            if textet[i:i + 2] == "{{" or textet[i:i + 2] == "[[":
                depth = depth + 1
                if depth == 2:  # si depth=1 és la plantilla principal
                               # si depth >2, és una plantilla dins una plantilla
                               # només ens interessa si és filla de la
                               # principal
                    ini_plantsec = i
                i = i + 2
                if i < len(textet):
                    continue
                else:
                    break
            if textet[i:i + 2] == "}}" or textet[i:i + 2] == "]]":
                if depth == 2:
                    fi_plantsec = i + 1
                    self.forats.append((ini_plantsec, fi_plantsec))
                depth = depth - 1
                if depth == 0:
                    final = i + 1  # no tinc clar que serveixi per res
                    break
                i = i + 2
                if i < len(textet):
                    continue
                else:
                    break
            i = i + 1
            if i < len(textet):
                continue
            else:
                break
        return i + 2

    def llistes_br(self):
        reg = r'(.*?)<\s*[Bb][Rr]\s*[\\\/ ]*>'
        regast = r'^\*.*'
        for p in self.llista_pars:
            if p.nom_param() == "peu" or p.nom_param() == "peu2":
                p.val_par = varglobals.treure_brs(p.valor_param().strip())
                continue
            valpar = p.valor_param().strip()
            outstr = ''
            lbrs = re.findall(reg, valpar, re.DOTALL)
            laster = re.findall(regast, valpar, re.MULTILINE)
            if len(laster) >= len(lbrs):
                continue
            trobada_llista_br = False
            mo = re.finditer(reg, valpar, re.DOTALL)
            for frase in mo:
                #print u"Frase és",frase.group(1)
                if len(frase.group(1)) > 0:
                    trobada_llista_br = True
                    # si ja tenia un asterisc, no l'afegim
                    if frase.group(1).lstrip()[0] != '*':
                        outstr = outstr + '* ' + frase.group(1).lstrip() + '\n'
                    else:
                        outstr = outstr + frase.group(1).lstrip() + '\n'
                else:
                    if trobada_llista_br:    # si no és la primera, ho fem igual
                        outstr = outstr + '* ' + frase.group(1) + '\n'
                ultim_match = frase.end(0)
            if trobada_llista_br:
                if ultim_match < len(valpar):
                        # si queda una cua de l'string, perquè no acaba en br, la posem
                        # strip final és per treure possibles \n a banda i
                        # banda
                    outstr = outstr + '* ' + valpar[ultim_match:].strip()
                # només posem un \n al principi de tot
                p.val_par = '\n' + outstr
                print(("Resultat llista_br ", p.val_par))


    def tractar_wikidata(self,nom_article):
        # si el nom és el mateix de l'article, el podem eliminar
        if self.get_par("nom") == nom_article:
            #print("********** ELIMINANT EL NOM **********************")
            self.elim_param("nom")

        # només si hi ha alguns paràmetres anirem a buscar wikidata

        par_item   = self.get_par("item")
        par_imatge = self.get_par("imatge")
        par_peu    = self.get_par("peu")
        par_datnai = self.get_par("data_naixement")
        par_llocna = self.get_par("lloc_naixement")
        par_datdef = self.get_par("data_defuncio")
        par_llocde = self.get_par("lloc_defuncio")

        if par_imatge != "" or par_peu    != "" or par_datnai != "" or \
           par_llocna != "" or par_datdef != "" or par_llocde != "" or \
           par_item   != "":

           wditem = varglobals.sel_itemwd(nom_article)

        # si hi ha paràmetre item i és el mateix de l'article, el podem treure
        if par_item != "":
            laq = wditem.get_id()
            if laq == qart:
                self.elim_param("item")

        # tractament de la imatge i el peu
        if par_imatge != "" or par_peu != "":
            #print("********** IMATGE O PEU **********************")
            # de moment no fem res, a espera de permís
            #self.mirar_imatge(nom_article,wditem)
            varglobals.foutrepassarimatges.write(nom_article)
            varglobals.foutrepassarimatges.write("\n")

        if par_datnai != "":
            #print("********** DATA DE NAIXEMENT **********************")
            valor = wditem.llegir_p_wd("P569")
            if valor is not None:
                self.elim_param("data_naixement")

        if par_llocna != "":
            #print("********** LLOC DE NAIXEMENT **********************")
            valor = wditem.llegir_p_wd("P19")
            if valor is not None:
                self.elim_param("lloc_naixement")

        if par_datdef != "":
            #print("********** DATA DE DEFUNCIO **********************")
            valor = wditem.llegir_p_wd("P570")
            if valor is not None:
                self.elim_param("data_defuncio")

        if par_llocde != "":
            #print("********** LLOC DE DEFUNCIO **********************")
            valor = wditem.llegir_p_wd("P20")
            if valor is not None:
                self.elim_param("lloc_defuncio")
        return

    def mirar_imatge(self, nom_article, wd):
        fitxer = self.get_par("imatge")
        peu = self.get_par("peu")

        print("som a mirar imatge")
        if fitxer == "":
            return
        if not fitxer_es_imatge(fitxer):
            print((
                "******** ATENCIO. Imatge " +
                fitxer +
                " no és una foto  **************"))

        commons = pywikibot.Site('commons', 'commons')
        # El try és per una reacció molt rara que té el pywikibot amb la imatge
        # del falciot negre
        wp_file = pywikibot.FilePage(commons, fitxer)
        try:
            fitxerexisteix = wp_file.exists()
        except pywikibot.exceptions.InconsistentTitleReceived:
            fitxerexisteix = True
        if not fitxerexisteix:
            print("************ ATENCIO. Imatge no és a commons **************")
        while True:
            try:
                sortim = not wp_file.isRedirectPage()
            except pywikibot.exceptions.InconsistentTitleReceived:
                sortim = True
                break
            if not sortim:
                print((
                    "El fitxer és una redirecció a",
                    wp_file.getRedirectTarget()))
                wp_file = wp_file.getRedirectTarget()
            else:
                break
        fitxer = wp_file.title(with_ns=False)

        #siteca = pywikibot.Site('ca')
        #pag = pywikibot.Page(siteca,nom_article)
        #wd = wdint.WDint()

        #itemwd = wd.wd_q_des_de_pag(pag)
        laq = wd.get_item().getID()
        llista_imatges = wd.imatge_i_peu('P18')
        fitxerawd = False
        if len(llista_imatges) > 0:
            primer_fitxer = llista_imatges[0][0]
            primer_peu = llista_imatges[0][1]
        else:
            primer_fitxer = primer_peu = ""

        # això ho fem per si és la segona passada del mateix article
        # en aquest cas, podria ser que esborréssim la imatge, si no té peu
        #algunencatala = False
        # for l in llista_imatges:
            # if l[1] > 0:
            #algunencatala = True

        for l in llista_imatges:
            # Mirem els diferents casos segons especificacions de Paucabot
            if varglobals.comp_fitx(fitxer, l[0]):
                fitxerawd = True     # el fitxer de la plantilla ja és a wikidata
            if varglobals.comp_fitx(fitxer, l[0]) and len(l[1]) > 0:
                # la imatge ja és a wikidata i té peu d'imatge,
                # ho eliminem de la plantilla només si és la primera de la
                # llista
                if varglobals.comp_fitx(primer_fitxer, l[0]):
                    print("eliminem imatge i peu perquè és el primer a wikidata")
                    self.elim_param("imatge")
                    self.elim_param("peu")
                else:
                    print(
                        "no eliminem imatge i peu perquè és a wikidata però no el primer")
            if varglobals.comp_fitx(fitxer, l[0]) and len(
                    peu) > 0 and l[1] == "":
                # la imatge és a wikidata, però no té peu d'imatge i nosaltres sí.
                # Haurem de posar el qualifier corresponent a la imatge.
                wd.act_wd_peu(fitxer, treure_markup(peu), 'P18')
                # Només eliminem imatge i peu si és el primer de la llista
                # si no, ens el quedem
                if varglobals.comp_fitx(primer_fitxer, l[0]):
                    print("eliminem imatge i peu havent posat peu a wikidata")
                    self.elim_param("imatge")
                    self.elim_param("peu")
            if peu == "" and len(l[0]) > 0:
                # No tenim peu d'imatge, i a Wikidata hi ha una foto. Preferim la
                # de Wikidata
                self.elim_param("imatge")
        # Ara ve el cas Carnotaure. A cawiki hi ha foto i peu de foto diferents de
        # Wikidata. Per tant, si no ho hem fet, carreguem el fitxer a Wikidata
        # amb el peu, però no esborrem els paràmetres de la plantilla.
        # A més, creem una llista d'articles amb aquest cas
        # ho fem si el nom del fitxer no és a Wikidata, i tenim imatge i peu
        if not fitxerawd and len(fitxer) > 0:  # and len(peu)>0:
            # ara mirem si el fitxer de la plantilla és a commons
            commons = pywikibot.Site('commons', 'commons')
            wp_file = pywikibot.FilePage(commons, fitxer)
            #print "ara anem a veure si existeix a Commons",fitxer
            try:
                fitxerexisteix = wp_file.exists()
            except pywikibot.exceptions.InconsistentTitleReceived:
                fitxerexisteix = True        # error estrany que dóna falciot negre
                print(
                    "Error de pywikibot ****************************************************")
            if fitxerexisteix:
                print("Fitxer no és a wikidata, actualitzem")
                wd.act_wd_imatge_peu(wp_file, treure_markup(peu))
                varglobals.foutimatges.write("|-\n")
                if primer_fitxer != "":
                    escrivim = "| [[" + varglobals.nom_article + "]]||" + "{{Q|" + laq + "}}|| [[Fitxer:" + \
                        fitxer + "|100px|" + peu + "]] ||" + peu + "||[[Fitxer:" + primer_fitxer + "|100px]]" + "\n"
                else:
                    escrivim = "| [[" + varglobals.nom_article + "]]||" + \
                        "{{Q|" + laq + "}}|| [[Fitxer:" + fitxer + "|100px|" + peu + "]] ||" + peu + "||\n"
                    print("Eliminem imatge i peu perquè a wikidata no hi havia res")
                    self.elim_param("imatge")
                    self.elim_param("peu")
                varglobals.foutimatges.write(escrivim)

    def mirar_peus_sense_imatge(self):
        if self.get_par("imatge").strip() == "":
            self.elim_param("peu")

    def set_par(self, nom, valor):
        for p in self.llista_pars:
            if p.nom_param().strip() == nom:
                p.set_valor(valor)
                return
        # si no existia el paràmetre, l'afegim
        self.llista_pars.append(
            Parametre(
                "",
                nom=nom,
                signeigual=True,
                valor=valor))

    def get_par(self, nom):
        for p in self.llista_pars:
            if p.nom_param().strip() == nom:
                temp = treu_comentari(p.valor_param())
                return temp.strip()
        return ""

    def troba_pars(self):
        cursor = len(self.titol) + 2
        self.llista_pars = []

        while cursor < len(self.text):
            if self.text[cursor] == "|":
                seguent = self.text[cursor + 1]
                if seguent != "|" and seguent != "}":
                    noupar = Parametre(self.text[cursor + 1:])
                    self.llista_pars.append(noupar)
                    lenpar = noupar.mida()
                    cursor = cursor + lenpar
            cursor = cursor + 1
        return

    def pintar(self):

        toret = "{{" + self.titol
        params_trobats = {}         # diccionari per detectar repeticions
        hihapars = False            # si hi ha algun paràmetre passarà a True
        maxlen = 0                  # per alinear els paràmetres
        # mirem quin és el paràmetre més llarg
        for parametre in self.llista_pars:
            act = len(parametre.nom_param())
            if (act > maxlen):
                maxlen = act

        # ara sí que pintem, recorrent tots els parametres que han quedat
        for parametre in self.llista_pars:
            hihapars = True
            # mirem quants espais falten per alinear tots els paràmetres
            act = len(parametre.nom_param())
            espais = maxlen - act
            if parametre.nom_param() in list(self.xl.params.keys()):
                # aquest paràmetre és dels esperats
                if parametre.nom_param() in params_trobats:
                    # aquest paràmetre ja havia sortit, avisem
                    varglobals.fout.write("|-\n")
                    escrivim = "| " + parametre.nom_param() + " REPETIT ||" + parametre.val_par + \
                        " ||[[" + varglobals.nom_article + "]]\n"
                    print(escrivim)
                    varglobals.fout.write(escrivim)
                else:
                    # apuntem per si torna a sortir
                    params_trobats[parametre.nom_param()] = parametre.val_par
                toret = toret + "\n| " + parametre.nom_param() + espais * ' '
            else:
                # aquest paràmetre no és dels esperats, avisem
                toret = toret + "\n| " + parametre.nom_param()
                varglobals.fout.write("|-\n")
                escrivim = "| " + parametre.nom_param() + "||" + parametre.val_par + \
                    " ||[[" + varglobals.nom_article + "]]\n"
                #print type(escrivim)
                #print escrivim
                varglobals.fout.write(escrivim)
            # ara anem a la resta. Primer l'igual
            if parametre.igual:
                toret = toret + " = "
                # ara el valor del paràmetre
                toret = toret + parametre.val_par
        if hihapars:
            toret = toret + "\n"
        # Tanquem la plantilla
        toret = toret + "}}"
        return toret

    def elim_param(self, par):
        #nova = [x for x in self.llista_pars if x.nom_param()!=par ]
        #self.llista_pars = nova
        nova = []
        for x in self.llista_pars:
            if x.nom_param() != par:
                nova.append(x)
            else:                # Avisem si esborrem referència
                lref = hiharef(x.valor_param())
                if lref > 0:
                    if lref > 25:
                        print(
                            (
                                "************* ATENCIO esborrem referència llarga amb nom ************************** " +
                                x.nom_param() +
                                " = " +
                                x.valor_param()))
                        self.refs_esborrades.append(
                            separar_refsambnom(x.valor_param()))
                    else:
                        print(
                            (
                                "************* ATENCIO esborrem referència curta amb nom ************************** " +
                                x.nom_param() +
                                " = " +
                                x.valor_param()))
        self.llista_pars = nova

    def aval_wd(self, wd):
        for parametre in self.llista_pars:
            p = self.xl.p_associada(parametre.nom_param())
            tipus = self.xl.tipus_associat(parametre.nom_param())
            print(("mirem p de", parametre.nom_param(), " és", p))
            resultat = wd.llegir_p_wd(p, tipus)

    def traduit(self):
        llista_nova = []
        # crearem una nova llista i la penjarem
        for parametre in self.llista_pars:
            # si és dels que s'han d'eliminar, ja el saltem
            if self.xl.eliminar(parametre.nom_param()):
                ln = hiharef(parametre.valor_param())
                if ln > 0:
                    if ln > 25:
                        print(
                            (
                                "************* ATENCIO esborrem referència llarga amb nom ************************** " +
                                parametre.nom_param() +
                                " = " +
                                parametre.valor_param()))
                        self.refs_esborrades.append(
                            separar_refsambnom(parametre.valor_param()))
                    else:
                        print(
                            (
                                "************* ATENCIO esborrem referència curta amb nom ************************** " +
                                parametre.nom_param() +
                                " = " +
                                parametre.valor_param()))
                continue
            # si no té informat el valor, també el saltem segons Paucabot
            if parametre.val_par.strip() == "":
                continue
            # si no, el traduim
            pnou = Parametre(
                "",
                nom=self.xl.traduir(
                    parametre.nom_param()),
                signeigual=parametre.igual,
                valor=parametre.val_par)
            llista_nova.append(pnou)
            #print(llista_nova)
        # si no l'hem trobada, tornem el text original sense canviar
        self.llista_pars = llista_nova

    def referenciesesborrades(self):
        return self.refs_esborrades

    def text(self):
        return self.text

    def mida(self):
        return len(self.text)

    def __repr__(self):
        toret = self.titol + "\n" + self.text  # això és unicode
        return toret

    def __init__(self, txt, nom, xl):
        final_plant = self.recalcular_forats(txt)
        self.text = txt[:final_plant]
        self.titol = nom
        self.troba_pars()
        self.refs_esborrades = []
        self.xl = xl
        self.pars_original = list(self.llista_pars)  # en creem una còpia

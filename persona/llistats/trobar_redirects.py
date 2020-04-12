# -*- coding: utf-8 -*-

#import query
#import wikipedia , re
import pywikibot, re, sys
import codecs
import pprint
 
def get_search_redirects(searchstr):
    pp = pprint.PrettyPrinter(indent=4)
    params = {
        'action'         :'query',
        'prop'           :'redirects',
        'rdprop'         :'title',
        'rdnamespace'    :'10',
        'titles'         :'Plantilla:'+searchstr,
	'rdlimit'        : 500,
	'continue'       :''
        }
#    print params
    l=[]
    lastContinue = {'continue': ''}
    while True:
       pr = params.copy()
       pr.update(lastContinue)
       sr=pywikibot.data.api.Request(**pr).submit()
       #pp.pprint(sr)
       if 'error' in sr:
          raise Exception(sr['error'])
       if 'warnings' in sr:
          raise Exception(sr['warnings'])
       pagines_font=sr['query']['pages']          # normalment serà una llista
                                            # d'un sol element
       for p in pagines_font:
         #pp.pprint(p)
         for i in pagines_font[p]['redirects']:
           l.append(i['title']) #.encode("utf-8"))
       if 'continue' not in sr:
          break
       lastContinue = sr['continue']
    return l

def get_search_articles(searchstr):
    params = {
        'action'         :'query',
        'list'           :'embeddedin',
        'eititle'        : searchstr,
        'eifilterredir'  :'nonredirects',
        'eilimit'        : 500,
        'einamespace'    :'0',
        'continue'       :''
        }
#    print params
    l=[]
    lastContinue = {'continue': ''}
    while True:
       pr = params.copy()
       pr.update(lastContinue)
       sr=pywikibot.data.api.Request(**pr).submit()
       if 'error' in sr:
          raise Exception(sr['error'])
       if 'warnings' in sr:
          raise Exception(sr['warnings'])
       for i in sr['query']['embeddedin']:
           l.append(i['title']) #.encode("utf-8"))
       if 'continue' not in sr:
          break
       lastContinue = sr['continue']
    return l

def main():
    if len(sys.argv)!=2:
       print u"Ús: python trobar_redirects.py <nom-de-la-plantilla>".encode("utf-8")
    else:
       l_masies = get_search_redirects(sys.argv[1])
       for p in l_masies:
          l_articles = get_search_articles(p)
          if len(l_articles)>0:
            print p.encode("utf-8")
            for a in l_articles:
              print a.encode("utf-8")
main()
pywikibot.stopme()

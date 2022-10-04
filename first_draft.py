# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:59:50 2022

@author: stanl
"""

import wikipediaapi
import pywikibot


def get_num_page_links(page_title, language='en'):
    wiki_wiki = wikipediaapi.Wikipedia(language)
    page = wiki_wiki.page(page_title)
    links = page.links
    
    return len(links)
    
def get_num_page_revisions(page_title, language='en'):
    site = pywikibot.Site(language, "wikipedia")
    page = pywikibot.Page(site, page_title)
    revs = [x for x in page.revisions()]
    
    return len(revs)

page_title = 'Python_(programming_language)'
num_links = get_num_page_links(page_title)
num_revisions = get_num_page_revisions(page_title)

print(f"Page '{page_title}' has {num_links} page links and {num_revisions} page revisions")

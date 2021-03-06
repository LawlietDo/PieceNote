# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 21:37:17 2017

@author: haochinnate
"""

import requests
from bs4 import BeautifulSoup


# use "requests" package to get the source code of webpage
url = "http://www.cpbl.com.tw/standing/year.html"
html = requests.get(url)

# use html.parser to analyze source code
sp = BeautifulSoup(html.text, "html.parser")
#print(sp) # all html content and tag

# title (the title of webpage, include the tag) 
pageTitle = sp.title
print(pageTitle)

# text (get the webpage text content after remove all tag)
pageContent = sp.text
# print(pageContent)

# find (return the first tag which match the condition)
firstH2 = sp.find("h2")
print(firstH2)
print()

# find_all (return all tags that match the condition)
allaTags = sp.find_all('a')
for aTag in allaTags:
    print(aTag)
    print("---")
print(len(allaTags))

#allH2Tags = sp.find_all('h2')
#for H2Tag in allH2Tags:
#    print(H2Tag)
#    print("---")
#print(len(allH2Tags))

# select (return the content of CSS selector)
titles = sp.select("title") # return a list
print(titles)

# find all <a> tag and class is "footer_link"
print(sp.find_all("a", {"class": "footer_link"}))

# find the <a> tag and its "href" property value is "/footer/contact/"
contactLink = sp.find("a", {"href":"/footer/contact/"})
print(contactLink)
print(contactLink.text) # the text of this tag

# all tag is "title" or "script"
#print(sp.find_all(["title","script"])) 

# to read the property(href) value of specific tag: get() method
for footerLinkTag in sp.find_all("a", {"class": "footer_link"}):
    print(footerLinkTag)
    print("the value of href property is: " + footerLinkTag.get("href"))
print()
      
      
      
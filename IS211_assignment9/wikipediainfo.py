#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""get the past value of apple stock"""

from re import L
import requests 
from bs4 import BeautifulSoup

def download(url):
    return requests.get(url).text

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/John_Heisman"
    text = download(url)
    soup = BeautifulSoup(text, features="lxml")
    #print(text)
    info = soup.find_all("table", class_="infobox vcard")
    #print(info)
    strip = (div.text.strip() for div in info)
    
    for i, strip in enumerate(strip):
        print(i, strip)
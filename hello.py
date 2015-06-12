__author__ = 'Sakuragi-Kun'
from bs4 import BeautifulSoup
import requests
import urllib2

s = requests.session()
url = "http://jobsnepal.com"
hell = s.get(url)
soup = BeautifulSoup(hell.text)
print soup.title.string


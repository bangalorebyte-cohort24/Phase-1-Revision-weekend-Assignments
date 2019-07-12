#!/usr/bin/env python3

import re

from bs4 import BeautifulSoup
import requests


base_url = 'http://oyc.yale.edu/'
resource_path = 'political-science/plsc-114#sessions'
original_url = base_url + resource_path

x = requests.get(original_url)
page = x.content

s = BeautifulSoup(page, 'html.parser')
all_td = s.find_all('td', class_="views-field-field-session-display-title-value")

for meow in all_td:
    print(base_url + str(meow.a.get('href')))

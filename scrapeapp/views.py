from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Page
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import datetime

def home(request):
    pages = Page.objects.filter(active=True)

    pagesList = []
    for page in pages:
        xml = urlopen(page.url)
        tree = ET.parse(xml)
        root = tree.getroot()
        #print(root)

        values = []
        count = 0
        for item in root[0].findall('item'):
            dic = {
                'title': item.find('title').text,
                'link': item.find('link').text,
                'date': item.find('pubDate').text,
            }
            print(item.find('pubDate').text)
            values.append(dic)
            count = count + 1
            if count > 10:
                break
        
        pageDict = {
            'name': page.name,
            'image': page.image,
            'values': values,
        }
        pagesList.append(pageDict)

    data = {
        'pages': pagesList
    }
    return render(request, 'index.html', data)
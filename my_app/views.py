from django.shortcuts import render
from requests.compat import quote_plus
from .models import Search
from googlesearch import search
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def home(request):
    return render(request, 'my_app/index.html')


def new_search(request):
    s = request.POST.get('search')
    # store seariching in db
    #Search.objects.create(search=s)

    response = []
    for r in search(s, tld='com', lang='en', stop=15):
        string = r.split('/')
        string = string[2].split('.')

        name = string[-2]
        if string[-2] == 'org':
            name = string[-3]

        response.append({
            'url': r, 
            'name': name
            })

    #response = requests.get(f'https://www.google.com/search?q={quote_plus(search)}')
    #data = response.text

    #soup = bs(data, features='html.parser')
    #links = soup.find_all('a')
        
    print(response)
    stuff = {
        'search': s,
        'results': response,
        }

    return render(request, 'my_app/new_search.html', stuff)
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def analyze(request):
    a = request.POST.get("text")

    inputs = request.POST.get('inputs', 'off')

    fullcaps = request.POST.get('fullcaps', 'off')
    charcount = request.POST.get('charcount', 'off')
    p = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}'''
    an = a

    if inputs == 'on':
        an = ''.join(char for char in a if char not in p)
    if fullcaps == 'on':
        an = an.upper()
    if charcount == 'on':
        count = f'Number of Characters: {sum(1 for char in an if not char.isspace())}'
    else:
        count = ''

    params = {'Purpose': 'Removed punctuations', 'analyzed_text': an, 'count': count}

    return render(request, 'analyze.html', params)

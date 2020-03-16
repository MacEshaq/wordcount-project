from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    usertext = request.GET['fulltext']
    text_dict = {}
    wordlist = usertext.split()
 
    for word in wordlist:

        if word in text_dict:
            text_dict[word] += 1

        else:
            text_dict[word] = 1

    sortedwords = sorted(text_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'usertext':usertext, 'count':len(wordlist), 'word_num':sortedwords})

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')
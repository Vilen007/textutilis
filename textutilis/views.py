from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def analyze(request):
    #get the text
    d = request.POST.get('text','default')
   #check check box value
    removepunc= request.POST.get('punc','off')
    cap = request.POST.get('cap','off')
    new = request.POST.get('new', 'off')
    space = request.POST.get('space', 'off')
    count = request.POST.get('count', 'off')
    if removepunc == "on":
        analyzed = ""
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in d:
            if char not in punctuation:
                analyzed = analyzed+char
        params = {'purpose':'Removed Punctuations', 'analyzed_text' : analyzed}
        d = analyzed
    if(cap=="on"):
        analyzed = ""
        for char in d:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        d = analyzed
    if (new == "on"):
        analyzed = ""
        for char in d:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        d = analyzed
    if (space == "on"):
        analyzed = ""
        for index,char in enumerate(d):
            if not(d[index] == " " and d[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        d = analyzed
    if (count == "on"):
        analyzed = 0
        for char in d:
            analyzed=analyzed+1
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
    if(removepunc != "on" and cap != "on" and new != "on" and space != "on" and count != "on"):
        return HttpResponse("error")
    return render(request, 'analyze.html', params)
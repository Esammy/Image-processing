from django.shortcuts import render

def votingTest(request):
    return render(request, 'votingsys.html')

def idSearch(request):
    return render(request, 'votinghome.html')
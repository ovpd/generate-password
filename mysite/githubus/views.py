from django.shortcuts import render

def git(request):
    return render(request, "githubus/githubus.html",{"Name": "Githubus"})

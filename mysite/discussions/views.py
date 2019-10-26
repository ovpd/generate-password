from django.shortcuts import render

def discussions_main(request):
    return render(request, "discussions/discussions.html",{"Name": "Discuss"})

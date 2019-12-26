from django.shortcuts import render


def basefun(request):

    return render(request,"index.html",{})

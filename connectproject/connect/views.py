from django.shortcuts import render
from .models import *

def index(request):

    tags = []

    s = Sport.objects.all()
    hl = Human_Language.objects.all()
    pl = Programming_Language.objects.all()
    p = Profession.objects.all()
    intr = Interest.objects.all()
    clg = CLGNIT.objects.all()


    for i in s:
        tags.append(i)

    for i in hl:
        tags.append(i)

    for i in pl:
        tags.append(i)

    for i in p:
        tags.append(i)

    for i in intr:
        tags.append(i)

    for i in clg:
        tags.append(i)


    if request.method == "POST":

        tag = request.POST.getlist("tags")
        print(tag)


        ru = []
        users = User.objects.all()

        for t in tag:
            for u in users:
                for tn in u.sport.all():
                    print(tn, t)
                    if t in tn.name:
                        ru.append(u) 

        return render(request, "connect/index.html", {
            "tags": tags,
            "users": ru

        })


    return render(request, "connect/index.html", {
        "tags": tags
    })
from django.shortcuts import render
from .models import *


ALL_TAGS = []
def define_all_tags():
    for tag in Sport.objects.all():
        ALL_TAGS.append(tag)

    for tag in Human_Language.objects.all():
        ALL_TAGS.append(tag)

    for tag in Programming_Language.objects.all():
        ALL_TAGS.append(tag)

    for tag in Profession.objects.all():
        ALL_TAGS.append(tag)

    for tag in Interest.objects.all():
        ALL_TAGS.append(tag)

    for tag in CLGNIT.objects.all():
        ALL_TAGS.append(tag)


ALL_USERS = {}
def setup_users():
    user_tags = []
    
    for user in User.objects.all():
        for item in user.sport.all():
            user_tags.append(item.name)
        for item in user.language.all():
            user_tags.append(item.name)
        for item in user.programming_language.all():
            user_tags.append(item.name)
        for item in user.profession.all():
            user_tags.append(item.name)
        for item in user.interest.all():
            user_tags.append(item.name)
        for item in user.clgnit.all():
            user_tags.append(item.name)

        ALL_USERS[user] = user_tags
        user_tags = []


define_all_tags()
setup_users()


def index(request):
    if request.method == "POST":
        submitted_tags = request.POST.getlist("tags")

        filtered_users = []
        for tag in submitted_tags:
            for user in ALL_USERS:
                if tag in ALL_USERS[user]:
                    filtered_users.append(user)

        return render(request, "connect/index.html", {
            "tags": ALL_TAGS,
            "users": filtered_users
        })

    return render(request, "connect/index.html", {
        "tags": ALL_TAGS
    })


def about(request):
    return render(request, "connect/layout.html")


def profile(request):
    return render(request, "connect/profile.html")


def individual_profile(request):
    return render(request, "connect/individual-profile.html")
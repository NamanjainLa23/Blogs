from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def my_page_by_number(request, month):
    return HttpResponse(month)

def my_page(request, month): #month is a variable used in challenges.urls file
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat no meat for the entire month"
    elif month == 'february':
        challenge_text = "Walk for at least 20 minutes every day"
    elif month == 'march':
        challenge_text = "Learn Django for at least 20 minutes every day"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)

def view(request):
    return HttpResponse("Hello, This is challenges page")

# def index_jan(request):
#     return HttpResponse("Hello, world. You're at the January challenges index.")
#
# def index_feb(request):
#     return HttpResponse("Hello, world. You're at the February challenges index.")
#
# def index_mar(request):
#     return HttpResponse("Hello, world. You're at the March challenges index.")
#
# def index_apr(request):
#     return HttpResponse("Hello, world. You're at the April challenges index.")
#
# def index_may(request):
#     return HttpResponse("Hello, world. You're at the May challenges index.")
#
# def index_jun(request):
#     return HttpResponse("Hello, world. You're at the June challenges index.")
#
# def index_jul(request):
#     return HttpResponse("Hello, world. You're at the July challenges index.")
#
# def index_aug(request):
#     return HttpResponse("Hello, world. You're at the August challenges index.")
#
# def index_sep(request):
#     return HttpResponse("Hello, world. You're at the September challenges index.")
#
# def index_oct(request):
#     return HttpResponse("Hello, world. You're at the October challenges index.")
#
# def index_nov(request):
#     return HttpResponse("Hello, world. You're at the November challenges index.")
#
# def index_dec(request):
#     return HttpResponse("Hello, world. You're at the December challenges index.")

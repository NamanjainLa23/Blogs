from django.urls import path
from . import views

#this is challenge specific urls file, we need to map it tp project specific urls file
urlpatterns = [
    path("", views.view), #if a request reaches / call view function from views
    # path("january",  views.index_jan), #if a request reaches /january call index function from views
    path("<int:month>", views.my_page_by_number),
    path("<str:month>", views.my_page)
    # path("february", views.index_feb),
    # path("march", views.index_mar)
    # path("april", views.index_apr),
    # path("may", views.index_may),
    # path("june", views.index_jun),
    # path("july", views.index_jul),
    # path("august", views.index_aug),
    # path("september", views.index_sep),
    # path("october", views.index_oct),
    # path("november", views.index_nov),
    # path("december", views.index_dec)
]

#setting each value manually is not a good practice, we can use loops to do this and add dynamically
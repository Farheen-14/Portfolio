from django.contrib import admin
from django.urls import path
from home import views 
urlpatterns = [
    # path('', views.index, name = 'bars'),
    # path("about", views.about, name = 'about'),
    # path("client", views.client, name = 'client'),
    path('', views.folio, name = 'bio')


    # path('add', views.add, name = 'add'),
    # path('sub', views.sub, name = 'sub')

    # for home page
    # path('', views.index, name = 'home'),
    # path("about", views.about, name = 'about')

]
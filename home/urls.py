from django.contrib import admin
from django.urls import path
from home import views 
urlpatterns = [
    # path('', views.index, name = 'bars'),
    # path("about", views.about, name = 'about'),
    # path("client", views.client, name = 'client'),
    path('', views.index, name = 'nav'),
    path('home', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('skills', views.skills, name = 'skills'),
    path('workexp', views.workexp, name = 'workexp'),
    path('education', views.educatiion, name = 'education'),
    path('contact', views.contact, name = 'contact'),
    path('footer', views.footer, name = 'footer')










    # path('add', views.add, name = 'add'),
    # path('sub', views.sub, name = 'sub')

    # for home page
    # path('', views.index, name = 'home'),
    # path("about", views.about, name = 'about')

]
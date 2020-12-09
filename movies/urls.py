from django.conf.urls import include, url
from . import views

app_name = 'movies'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^search/', views.search_autocomplete, name='search'),
    url(r'^logout/', views.logout_user, name='logout'),
    url(r'^add_movies/', views.add_movies, name='add_movies'),
    url(r'^all_movies/', views.show_movies, name='all_movies'),
    url(r'^add_timing/(?P<movie_id>[0-9]+)/', views.add_timing, name='add_timing'),
    url(r'^timing/', views.timing, name='timing'),
    url(r'^purchase/(?P<movie_id>[0-9]+)', views.purchase, name='purchase'),

]

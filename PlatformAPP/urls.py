from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('docummentation', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('event', views.event, name='event'),
    path('event-details', views.event_details, name='event-details'),
    path('event-carousel', views.event_carousel, name='event-carousel'),
    path('faq', views.faq, name='faq'),
    path('', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
    path('index4', views.index4, name='index4'),
    path('indexFour', views.indexFour, name='indexFour'),
    path('indexOne', views.indexOne, name='indexOne'),
    path('indexThree', views.indexThree, name='indexThree'),
    path('indexTwo', views.indexTwo, name='indexTwo'),
    path('news', views.news, name='news'),
    path('news-carousel', views.news_carousel, name='news-carousel'),
    path('news-details', views.news_details, name='news-details'),
    path('news-grid', views.news_grid, name='news-grid'),
    path('pricing', views.pricing, name='pricing'),
    path('program', views.program, name='program'),
    path('program-carousel', views.program_carousel, name='program-carousel'),
    path('program-details', views.program_details, name='program-details'),
    path('team', views.team, name='team'),
    path('team-carousel', views.team_carousel, name='team-carousel'),
    path('team-details', views.team_details, name='team-details'),
    path('404', views.NotfoundPage, name='404'),
    path('contactP', views.ContactPHP, name='contactP'),


]

from django.urls import path
from . import views

app_name = 'botapp'
urlpatterns = [
    # path('jobpositions/', views.JobposView.as_view(), name='jobpos'),
    path('webhook/', views.webhook, name='webhook'),
     path('', views.index, name='index'),
    path('collect_coin/', views.collect_coin, name='collect_coin'),
]
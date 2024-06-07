from django.urls import path
from lojinha import views

app_name= 'lojinha'
urlpatterns = [
    path('',views.index,name='index.html')
    
]

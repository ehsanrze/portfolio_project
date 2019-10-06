from django.urls import path , include
from .views import blog , detail_blog
urlpatterns = [
    path('', blog),
    path ('<int:id>' , detail_blog , name = 'detail'),
] 

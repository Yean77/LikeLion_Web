from django.urls import path
from . import views

urlpatterns = [
    path('class/',views.about_me),
    path('', views.landing),
    path('naverclass/',views.naver),
    path('youtube/',views.youtube),
    path('24class/',views.korea),
    path('about/',views.about),
    path('class/classdetail1',views.classdetail1),
    path('class/classdetail2',views.classdetail2),

]
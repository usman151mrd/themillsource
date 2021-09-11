from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('home/', views.home_page),
    path('about-us/', views.about_us_page)
]

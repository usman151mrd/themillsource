from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('detail/<int:pk>/', views.detail_page, name='detail'),
    path('home/', views.home_page,name='home'),
    path('about-us/', views.about_us_page, name='about-us'),
    path('write-for-us/', views.write_for_us_page, name='write-for-us'),
    path('send-us-your-pr/', views.send_us_your_pr_page, name='send-us-your-pr'),
    path('advertise/', views.advertise_page, name='advertise'),
]

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    #  path('', views.IndexView.as_view()),

    path('detail/<int:pk>/', views.detail_page, name='detail'),
    path('', views.home_page,name='home'),
    path('about-us/', views.about_us_page, name='about-us'),
    path('what-drives-us/', views.about_us_page_two, name='what-drives-us'),
    path('our-advertising-partners/', views.about_us_page_three, name='our-advertising-partners'),
    path('make-money-with-us/', views.about_us_page_four, name='make-money-with-us'),
    path('write-for-us/', views.write_for_us_page, name='write-for-us'),
    path('send-us-your-pr/', views.send_us_your_pr_page, name='send-us-your-pr'),
    path('advertise/', views.advertise_page, name='advertise'),
    path('temp/', views.write_for_us_page, name='temp'),
    path('contact-us',view=views.contact_us, name='contact-us'),
    path('article-page/<int:menu_id>/',view=views.article_page, name='article-page')
]

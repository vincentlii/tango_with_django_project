from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/',
        views.show_category, name='show_category'),  # category_name_slug is what we pass through to the view's 'show_category()'
]
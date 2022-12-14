from django.urls import path
from search import views, ml

app_name = 'search'
urlpatterns = [
     path('', views.keyword),
     path('recommend/', views.predict),
     path('beerprofile/<int:pk>/', views.search_detail, name="beerprofile"),
     path('search/', views.search),
     path('ranking/', views.ranking),
     path('like/<int:pk>/', views.like, name="like")
     # path('beer/', views.beer)
]

    
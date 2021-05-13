from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.apiurlsoverview,name='api-urls'),
    path('stock-list/',views.stocklist,name='stock-list'),
    path('stock-detail/<str:pk>/',views.stockdetail,name='stock-detail'),
    path('stock-create/',views.stockcreate,name='stock-create'),
    path('stock-update/<str:pk>/',views.stockupdate,name='stock-update'),
    path('stock-delete/<str:pk>/',views.stockdelete,name='stock-delete'),

]
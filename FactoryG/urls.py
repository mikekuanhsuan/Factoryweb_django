from django.contrib import admin
from django.urls import path, include

from Product.views import factory_list 
from login.views import login_list, home, my_view
from Mill.views import mill_report, mill_chart_list

urlpatterns = [
    path('', login_list, name='default-login'),
    path('login_list/', login_list, name='login_list'),
    path('factories/', factory_list, name='factory-list'),
    
    path('home/Index/', home, name='home_index'),
    # path('login_check/', login_check, name='login_check'),
    path('my-view/', my_view, name='my-view'),
    path('Mill/<str:day>/<str:millId>/<str:factoryId>/', mill_report, name='Mill'),
    path('mill_chart_list/', mill_chart_list, name='Mill_ChartList'),
]

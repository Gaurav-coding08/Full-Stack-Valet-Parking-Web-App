from django.urls import path
from .views import car_info_create_api_view,admin_info_create_api_view,getalladmininfo,getallcarinfo

urlpatterns = [
    path("adminaccess/<str:pk>/",admin_info_create_api_view.as_view(),name='admin_view'),
    path("car/<str:pk>",car_info_create_api_view.as_view(),name='car_view'),
    path("adminaccess/",getalladmininfo,name='get_all_admin_info'),
    path("carinfo/",getallcarinfo,name='get_all_car_info')
]
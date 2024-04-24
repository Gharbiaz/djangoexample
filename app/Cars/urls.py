from django.urls import path
from . import views
urlpatterns = [
    path('car_list/', views.CarList.as_view(), name='car_list'),
    path('view/<int:pk>', views.CarDetail.as_view(), name='car_detail'),
    path('new', views.CarCreate.as_view(), name='car_new'),
    path('edit/<int:pk>', views.CarUpdate.as_view(), name='car_edit'),
    path('delete/<int:pk>', views.CarDelete.as_view(), name='car_delete'),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
]

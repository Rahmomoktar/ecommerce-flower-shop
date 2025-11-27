from django.urls import path

from Project import settings
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    # path('Contact_Us/',views.contact_us,name='Contact_Us'),
    path('contact_us/', views.contact_us, name='contact_us'),
     path('SpecialFlower_view/',views.SpecialFlower_view,name='SpecialFlower'),

    path('products/',views.products,name='products'),
    path('login/', views.login_view, name='login'),
    path('logout_view/',views.logout_view,name="logout"),
    path('register/', views.register_view, name='register'),


    # booking

    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/create/', views.booking_create, name='booking_create'),
    path('bookings/update/<int:pk>/', views.booking_update, name='booking_update'),
    path('bookings/delete/<int:pk>/', views.booking_delete, name='booking_delete'),



    # oder

    path('order/', views.order_list, name='order_list'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('order/new/', views.order_create, name='order_create'),
    path('order/<int:pk>/edit/', views.order_update, name='order_update'),
    path('order/<int:pk>/delete/', views.order_delete, name='order_delete'),

]

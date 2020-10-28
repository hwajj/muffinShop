from django.urls import path

from . import views


app_name = 'muffinShop'
urlpatterns = [

    # ex.  /muffinShop/
    path('', views.index,  name='index'),
    #path('', views.IndexView.as_view(), name='index'),

    path('order/', views.new_order, name='new_order'),
    #ex./muffinShop/order

   # path('order/', views.order, name='order'),
    #path('order/',views.ConfirmView.as_view(),  name='order'),

    # ex./muffinShop/2/order
    path('order/confirm', views.order_confirm ,name='order_confirm'),

    # ex./muffinShop/check
    path('check/', views.check, name='check'),

    # ex./muffinShop/check_order
    path('check_order', views.check_order, name='check_order'),
    path('test' ,views.test, name='test')

]
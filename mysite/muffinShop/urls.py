from django.urls import path

from . import views


app_name = 'muffinShop'
urlpatterns = [

    # ex.  /muffinShop/
    path('', views.index,  name='index'),
    #path('', views.IndexView.as_view(), name='index'),

    path('order/', views.order, name='order'),
    #ex./muffinShop/order


    # ex./muffinShop/order/confirm
    path('order/confirm', views.confirm ,name='confirm'),

    # ex./muffinShop/check
    path('check/', views.check, name='check'),

    # ex./muffinShop/check_order
    path('check_order', views.check_order, name='check_order'),
    path('test' ,views.test, name='test')

]
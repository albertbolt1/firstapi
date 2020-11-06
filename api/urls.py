from django.urls import path,include
from django.conf.urls import url 
from . import views
urlpatterns = [ 
    url(r'^api/pizzas$', views.pizza_list),
    url(r'^api/pizzas/(?P<pk>[0-9]+)$', views.pizza_detail),
    url(r'^api/pizzas/veg_nonveg$', views.pizza_list_veg_nonveg)
]
from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prodt_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.proddetail,name='detail'),
    path('search',views.searching,name='search')


]
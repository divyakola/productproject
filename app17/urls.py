from django.urls import path,re_path
from .views import product_insert,display
urlpatterns = [
    path('pinsert',product_insert),
    path('show',display)

]
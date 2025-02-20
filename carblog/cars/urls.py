from django.urls import path
from .views import *

urlpatterns = [
    path('', CarsHome.as_view(), name='home'),
    path('about/', show_about, name='about'),
    path('car/<slug:car_slug>', ShowCar.as_view(), name='car'),
    path('category/<slug:cat_slug>', CarCategory.as_view(), name='category'),
    path('addblog/', CreateBlog.as_view(), name='newblog'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

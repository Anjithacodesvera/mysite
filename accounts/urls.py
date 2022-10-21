from django.urls import path

from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import  function_r
# from accounts import views as accounts_view
from .views import Signup

urlpatterns = [
    # path('', views.Login, name='login'),
    # path('register/', views.register, name='register'),
    # path('login/',views.Login, name='login'),
    # path('signup/', accounts_view.methods, name='methods'),
    path('page/', views.function_r, name='function'),
    path('signup/',views.methods,name='methods'),
    path('login/',views.Login.as_view(),name='hello'),
    path('ajaxcall', views.ajaxcall.as_view()),
    path('ajax-home', views.ajaxhome),
    path('home',views.home,name='home'),


]
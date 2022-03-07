# from django.contrib import admin
from django.urls import path,include
from . import views

app_name='auth_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home_view, name='home_view'),
    path('javaexam/',views.javaexam_view, name='javaexam_view'),
    path('pythonexam/',views.pythonexam_view, name='pythonexam_view'),
    path('signup/',views.signup_view, name='signup_view'),
    path('logout/',views.logout_view, name='logout_view'),
    path('accounts/', include('django.contrib.auth.urls')),
]

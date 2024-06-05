from django.contrib import admin
from django.urls import path
from . views import download_data
from . import views

urlpatterns = [
    path ('',views.index,name = 'index'),
    path('users/login', views.login_view, name='login'),
    path('admin/', admin.site.urls),
    path('upload_sensor/',views.upload_sensor_data,name='upload sensor'),
    path('upload_page/',views.upload_page_data,name='upload page'),
    path('data/',views.get_sensor_data),
    path('get_data/<str:Cant_Base>',views.get_sensor_data,name = 'Get Data'),
    path('contact', views.contact, name='contact'),
    path('visualizacion', views.visualizacion, name='visualizacion'),
    path('about', views.about, name='about'),
    path('download_data', download_data, name='download_data'),
]

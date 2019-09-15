from django.urls import path
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.Fibonacci,name='Fibonacci-home'),
    path('result',views.result,name='Fibonacci-result'),


]
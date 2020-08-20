from django.urls import path
from app11 import views
app_name="app11"


urlpatterns = [
    path('builtins/',views.builtins,name="biltins"),

]

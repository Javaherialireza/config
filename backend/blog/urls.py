from django.urls import path  ,include
from .views import Articlelist
app_name = "blog"

urlpatterns = [
    path('' ,Articlelist.as_view(), name="list")

]
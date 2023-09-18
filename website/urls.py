from django.urls import path
from website.views import home, training, couress

urlpatterns = [
    path("", home, name="home"),
    path("training", training, name="training"),
    path("coures", couress, name="coures"),
]

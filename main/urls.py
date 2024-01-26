from django.urls import path
from .views import *
urlpatterns =[
    path('GetBanner/', GetBanner),
    path('GetRecomendation/', GetRecomendation),
    path('GetSell/', GetSell),
    path('GetDetail/' ,GetDetail),
    path('GetPresintaiton/' ,GetPresintaiton),
    path('GetTestimonial/',GetTestimonial),
    path('GetAbout_us/',GetAbout_us),

]
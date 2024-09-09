from django.urls import path

from . import views

app = 'officialwebsite'

urlpatterns = [
    path('',views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('chisipite/', views.chisipite, name='chisipite'),
    path('grange/', views.grange, name="grange"),
    path('hogerty/', views.hogerty, name="hogerty"),
    path('brooke/', views.brooke, name="brooke"),
    path('bvumba/', views.bvumba, name='bvumba'),
    path('carrick/', views.carrick, name='carrick'),
    path('marlbo/', views.marlbo, name='marlbo'),
    path('gym/', views.gym, name='gym')
]
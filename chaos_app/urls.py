from django.urls import path
from . import views
urlpatterns = [

    path('api/generate_and_save_tent_map/', views.generate_and_save_tent_map, name='generate_and_save_tent_map'),
    path('api/generate_and_save_logistic_map/', views.generate_and_save_logistic_map, name='generate_and_save_logistic_map'),
    path('api/generate_and_save_complex_squaring_map/', views.generate_and_save_complex_squaring_map, name='generate_and_save_complex_squaring_map'),

    path('api/generate_and_save_bernoulli_map/', views.generate_and_save_bernoulli_map, name='generate_and_save_bernoulli_map'),
    path('api/generate_and_save_lorenz96_map/', views.generate_and_save_lorenz96_map, name='generate_and_save_lorenz96_map'),

    path('api/lorenz_map/', views.lorenz_map, name='lorenz_map'),
    path('api/poincare_map/', views.poincare_map_view, name='poincare_map'),
    path('api/generate_tinkerbell_map/', views.generate_and_save_tinkerbell_map, name='generate_tinkerbell_map'),
    path('api/generate_gingerbread_map/', views.generate_and_save_gingerbread_map, name='generate_gingerbread_map'),
    path('api/generate_logistic_map/', views.generate_and_save_logistic_map, name='generate_logistic_map'),

    path('api/generate_and_save_gauss_map/', views.generate_and_save_gauss_map,name='generate_and_save_gauss_map'),
    path('api/generate_and_save_lotka_volterra_map/', views.generate_and_save_lotka_volterra_map, name='generate_and_save_lotka_volterra_map'),

]


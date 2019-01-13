from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ruleform/', views.rule_form_view, name='ruleform'),
    path('ruleformedit/<int:pk>', views.rule_form_edit, name='ruleformedit'),
]

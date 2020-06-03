from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'web'

urlpatterns = [
    path('', TemplateView.as_view(template_name='web/home.html'), name='home'),

    path('keeper/login/', TemplateView.as_view(template_name='web/keeper/login.html'), name='keeper-login'),
    path('keeper/er/nueva-cuenta/', TemplateView.as_view(template_name='web/keeper/er/new.html'), name='keeper-new-er'),
    path('keeper/er/nueva-cuenta-ok/', TemplateView.as_view(template_name='web/keeper/er/new-ok.html'), name='keeper-new-er-ok'),
    path('keeper/er/tareas/', TemplateView.as_view(template_name='web/keeper/er/tasks.html'), name='keeper-er-tasks'),
    path('keeper/er/email/', TemplateView.as_view(template_name='web/keeper/er/email.html'), name='keeper-er-email'),
    path('keeper/er/datos-cd/', TemplateView.as_view(template_name='web/keeper/er/cd-form.html'), name='keeper-cd-form'),

    path('er/login/', TemplateView.as_view(template_name='web/er/login.html'), name='er-login'),
    path('er/inicio/', TemplateView.as_view(template_name='web/er/home.html'), name='er-home'),
    path('er/usuarios/', TemplateView.as_view(template_name='web/er/users/list.html'), name='er-users-list'),
    path('er/usuarios/enviar-invitacion', TemplateView.as_view(template_name='web/er/users/form.html'), name='er-users-invitation'),
    path('er/productos/', TemplateView.as_view(template_name='web/er/products/list.html'), name='er-products-list'),
    path('er/productos/certificado-persona-natural', TemplateView.as_view(template_name='web/er/products/form.html'), name='er-products-edit'),
]
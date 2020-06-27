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

    path('keeper/admin/', TemplateView.as_view(template_name='web/keeper/admin/home.html'), name='keeper-admin'),
    path('keeper/admin/users/', TemplateView.as_view(template_name='web/keeper/admin/users/list.html'), name='keeper-users-list'),
    path('keeper/admin/users/form/', TemplateView.as_view(template_name='web/keeper/admin/users/form.html'), name='keeper-users-add'),
    
    path('keeper/admin/ers/', TemplateView.as_view(template_name='web/keeper/admin/ers/list.html'), name='keeper-ers-list'),
    path('keeper/admin/ers/paino', TemplateView.as_view(template_name='web/keeper/admin/ers/detail.html'), name='keeper-er-detail'),

    path('er/login/', TemplateView.as_view(template_name='web/er/login.html'), name='er-login'),    
    path('er/inicio/', TemplateView.as_view(template_name='web/er/home.html'), name='er-home'),
    path('er/config/', TemplateView.as_view(template_name='web/er/config.html'), name='er-config'),
    path('er/usuarios/enviar-mail/', views.invite_user, name='er-users-invitation'),
    # path('er/usuarios/enviar-invitacion', TemplateView.as_view(template_name='web/er/users/form.html'), name='er-users-invitation'),

    path('er/usuarios/', TemplateView.as_view(template_name='web/er/users/list.html'), name='er-users-list'),

    path('er/productos/', TemplateView.as_view(template_name='web/er/products/list.html'), name='er-products-list'),
    path('er/productos/certificado-persona-natural', TemplateView.as_view(template_name='web/er/products/form.html'), name='er-products-edit'),
    path('er/agencias/', TemplateView.as_view(template_name='web/er/ars/list.html'), name='er-ars-list'),
    path('er/agencias/gonzales/', TemplateView.as_view(template_name='web/er/ars/detail.html'), name='er-ar-detail'),
    path('er/ordenes/', TemplateView.as_view(template_name='web/er/orders/list.html'), name='er-orders-list'),
    path('er/ordenes/detail/', TemplateView.as_view(template_name='web/er/orders/detail.html'), name='er-orders-detail'),
    
    path('er/agencia/', TemplateView.as_view(template_name='web/er/ars/login.html'), name='er-ar-login'),
    path('er/nueva-agencia/', TemplateView.as_view(template_name='web/er/new-ar.html'), name='er-new-ar'),
    path('er/agencia/tareas/', TemplateView.as_view(template_name='web/er/ar/tasks.html'), name='er-ar-tasks'),

    path('sendgrid-webhook/', views.sendgrid_webhook, name='sendgrid-webhook')
]
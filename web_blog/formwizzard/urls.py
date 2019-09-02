from django.urls import path, re_path
from . import views
app_name = 'formwizzard'

urlpatterns = [
    path('', views.FormWizardView.as_view(), name='mpform'),
]

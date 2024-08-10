from django.urls import path
from .views import handle_form_data,process_data_for_value
urlpatterns = [
    path('form/',handle_form_data,name="handle_form"),
    path('machine/',process_data_for_value),
]

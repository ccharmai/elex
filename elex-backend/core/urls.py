from django.urls import path
from . import views

urlpatterns = [
	# auth part
	path('token.get/', views.api_token_get),
	path('token.info/', views.api_token_info),

	# person part
	path('person.create/', views.api_person_create),
]

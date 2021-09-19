from django.urls import path
from . import views

urlpatterns = [
	# auth part
	path('token.get/', views.api_token_get),
	path('token.info/', views.api_token_info),
	path('token.delete/', views.api_token_delete),

	path('person.create/', views.api_person_create),

	path('get.makers/', views.api_get_makers),
	path('get.types/', views.api_get_types),
	path('get.elements/', views.api_get_elements),
	path('get.modifications/', views.api_get_modifications),

	path('adm/get.users/', views.api_admin_get_users),
	path('adm/set.user/', views.api_admin_set_user),
]

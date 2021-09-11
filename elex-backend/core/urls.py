from django.urls import path
from . import views

urlpatterns = [
	# auth part
	path('token.get/', views.api_token_get),
	path('token.info/', views.api_token_info),
	path('token.delete/', views.api_token_delete),

	# person part
	path('person.create/', views.api_person_create),

	# simple table
	#path('get.library/', views.api_get_library),

	path('get.makers/', views.api_get_makers),
	#path('add.makers/', views.api_add_makers),

	path('get.types/', views.api_get_types),
	#path('add.types/', views.api_add_types),

	path('get.elements/', views.api_get_elements),
	#path('add.elements/' , views.api_add_elements),

	path('get.modifications/', views.api_get_modifications),
	#path('add.modifications/', views.api_add_modifications),

	#path('get.properties/', views.api_get_properties),
	#path('add.properties/', views.api_add_properties),
]

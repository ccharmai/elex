from django.urls import path
from . import views

urlpatterns = [
	# auth part
	path('token.get/', views.api_token_get),
	path('token.info/', views.api_token_info),

	# person part
	path('person.create/', views.api_person_create),

	# simple table
	path('get.table/', views.api_get_table),

	path('get.makers/', views.api_get_makers),
	path('add.makers/', views.api_add_makers),

	path('get.types/', views.api_get_types),
	path('add.types/', views.api_add_types),

	path('get.items/', views.api_get_items),
	path('add.items/' , views.api_add_items),

	path('get.modifications/', views.api_get_modifications),
	path('add.modifications/', views.api_add_modifications),

	path('get.properties/', views.api_get_properties),
	path('add.properties/', views.api_add_properties),
]

from django.urls import path
from . import views

urlpatterns = [
	# auth part
	path('token.get/', views.api_token_get),
	path('token.info/', views.api_token_info),
	path('token.delete/', views.api_token_delete),

	path('person.create/', views.api_person_create),
	path('person.change_password/', views.api_person_change_password),

	path('get.makers/', views.api_get_makers),

	path('get.types/', views.api_get_types),

	path('get.elements/', views.api_get_elements),
	path('add.element/', views.api_add_element),

	path('get.modifications/', views.api_get_modifications),
	path('add.modification/', views.api_add_modification),

	path('get.properties/', views.api_get_properties),

	path('adm/get.users/', views.api_admin_get_users),
	path('adm/set.user/', views.api_admin_set_user),
	path('adm/del.user/', views.api_person_delete),
]

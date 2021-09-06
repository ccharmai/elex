from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
import json

from .auth import get_person_from_req, create_token
from .validators import validate_new_user
from .models import Person, Token, Maker, Type, Item, Modification, Property, Log


def post_json(request):
	try:
		json_str=((request.body).decode('utf-8'))
		json_obj=json.loads(json_str)
		return json_obj
	except:
		return None


@csrf_exempt
@require_POST
def api_token_get(request):
	req = post_json(request)
	try:
		name = req['name']
		password = req['password']
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Name or password not passed', 'msg': 'Не переданы имя пользователя или пароль' })
	status, token, person = create_token(name, password)
	if not status: return JsonResponse({ 'status': 'fail', 'reason': 'Invalid name or password', 'msg': 'Неверное имя пользователя или пароль' })
	return JsonResponse({ 'status': 'ok', 'name': person.name, 'isAdmin': person.is_admin, 'token': token })


@csrf_exempt
@require_POST
def api_token_info(request):
	req = post_json(request)
	try:
		token = req['token']
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Token not passed', 'msg': 'Не передан токен'})
	person = get_person_from_req(req)
	if not person: return JsonResponse({ 'status': 'fail', 'reason': 'Invalid token', 'msg': 'Неверный токен' })
	return JsonResponse({ 'status': 'ok', 'name': person.name, 'isAdmin': person.is_admin })


@csrf_exempt
@require_POST
def api_person_create(request):
	req = post_json(request)
	try:
		name = req['name']
		password = req['password']
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Name or password not passed', 'msg': 'Не передано значение имени или пароля' })
	if req.__contains__('description'): description = req['description']
	else: description = None
	status = validate_new_user(name)
	if not status: return JsonResponse({ 'status': 'fail', 'reason': 'Name taken', 'msg': 'Имя пользователя занято' })
	Person(name=name, password=make_password(password), description=description).save()
	return JsonResponse({ 'status': 'ok' })


@csrf_exempt
@require_POST
def api_get_makers(request):
	req = post_json(request)
	all_objs = Maker.objects.filter(is_visible=True)
	serialized_data = []
	for i in all_objs:
		serialized_data.append({
			'id': i.id,
			'name': i.name,
			'description': i.description,
		})
	return JsonResponse({ 'status': 'ok', 'makers': serialized_data })


@csrf_exempt
@require_POST
def api_add_makers(request):
	req = post_json(request)
	try:
		name = req['name']
		description = req['description']
		token = req['token']
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Name or description or token not passed', 'msg': 'Не пердано значение имени, токена или описания (описание может быть пустое)' })
	if not name or not token: return JsonResponse({ 'status': 'fail', 'reason': 'Empty name',  'msg': 'Пустое значение имени или токена' })
	person = get_person_from_req(req)
	if not person: return JsonResponse({ 'status': 'fail', 'reason': 'No auth', 'msg': 'пользователь не авторизован' })
	obj = Maker(name=name, description=description, is_visible=False)
	if person and person.is_admin: obj.is_visible = True
	obj.save()
	return JsonResponse({ 'status': 'ok', 'visible': obj.is_visible, 'id': obj.id })


@csrf_exempt
@require_POST
def api_get_types(request):
	req = post_json(request)
	all_objs = Type.objects.filter(is_visible=True)
	serialized_data = []
	for i in all_objs:
		serialized_data.append({
			'id': i.id,
			'name': i.name,
			'description': i.description,
		})
	return JsonResponse({ 'status': 'ok', 'types': serialized_data })


@csrf_exempt
@require_POST
def api_add_types(request):
	req = post_json(request)
	try:
		name = req['name']
		description = req['description']
		token = req['token']
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Name or description or token not passed', 'msg': 'Не пердано значение имени, токена или описания (описание может быть пустое)' })
	if not name or not token: return JsonResponse({ 'status': 'fail', 'reason': 'Empty name',  'msg': 'Пустое значение имени или токена' })
	person = get_person_from_req(req)
	if not person: return JsonResponse({ 'status': 'fail', 'reason': 'No auth', 'msg': 'пользователь не авторизован' })
	obj = Type(name=name, description=description, is_visible=False)
	if person and person.is_admin: obj.is_visible = True
	obj.save()
	return JsonResponse({ 'status': 'ok', 'visible': obj.is_visible, 'id': obj.id })


@csrf_exempt
@require_POST
def api_get_items(request):
	req = post_json(request)
	all_objs = Item.objects.filter(is_visible=True)
	serialized_data = []
	for i in all_objs:
		serialized_data.append({
			'id': i.id,
			'name': i.name,
			'maker': {
				'id': i.maker.id,
				'name': i.maker.name,
				'description': i.maker.description,
			},
			'type': {
				'id': i.type.id,
				'name': i.type.name,
				'description': i.type.description,
			},
		})
	return JsonResponse({ 'status': 'ok', 'items': serialized_data })


@csrf_exempt
@require_POST
def api_add_items(request):
	req = post_json(request)
	try:
		name = req['name']
		maker = req['maker']
		_type = req['type']
		token = req['token']
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Name or maker id or type id or token not passed', 'msg': 'Не пердано значение имени, токена, производителя или типа' })
	if not name or not token or not maker or not _type: return JsonResponse({ 'status': 'fail', 'reason': 'Empty name, maker, type or token',  'msg': 'Пустое значение имени, токена, производителя или типа' })
	person = get_person_from_req(req)
	if not person: return JsonResponse({ 'status': 'fail', 'reason': 'No auth', 'msg': 'пользователь не авторизован' })
	try:
		maker = Maker.objects.get(id=maker)
		_type = Type.objects.get(id=_type)
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Maker of type not found', 'msg': 'Передано несуществующее значения id производителя или типа' })
	obj = Item(maker=maker, type=_type, name=name, is_visible=False)
	if person and person.is_admin: obj.is_visible = True
	obj.save()
	return JsonResponse({ 'status': 'ok', 'visible': obj.is_visible, 'id': obj.id })


@csrf_exempt
@require_POST
def api_get_modifications(request):
	req = post_json(request)
	all_objs = Modification.objects.filter(is_visible=True)
	serialized_data = []
	for i in all_objs:
		serialized_data.append({
			'id': i.id,
			'name': i.name,
			'item': {
				'name': i.item.name,
				'maker': {
					'id': i.item.maker.id,
					'name': i.item.maker.name,
					'description': i.item.maker.description,
				},
				'type': {
					'id': i.item.type.id,
					'name': i.item.type.name,
					'description': i.item.type.description,
				},
			}
		})
	return JsonResponse({ 'status': 'ok', 'modifications': serialized_data })


@csrf_exempt
@require_POST
def api_add_modifications(request):
	req = post_json(request)
	try:
		name = req['name']
		item = req['item']
		token = req['token']
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Name or item id or token not passed', 'msg': 'Не пердано значение имени, токена или компонента' })
	if not name or not token or not item: return JsonResponse({ 'status': 'fail', 'reason': 'Empty name, items or token',  'msg': 'Пустое значение имени, токена или компонента' })
	person = get_person_from_req(req)
	if not person: return JsonResponse({ 'status': 'fail', 'reason': 'No auth', 'msg': 'пользователь не авторизован' })
	try:
		item = Item.objects.get(id=item)
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Item not found', 'msg': 'Передано несуществующее значения id компонента' })
	obj = Modification(item=item, name=name, is_visible=False)
	if person and person.is_admin: obj.is_visible = True
	obj.save()
	return JsonResponse({ 'status': 'ok', 'visible': obj.is_visible, 'id': obj.id })


@csrf_exempt
@require_POST
def api_get_properties(request):
	req = post_json(request)
	all_objs = Property.objects.filter(is_visible=True).order_by('modification')
	serialized_data = []
	for i in all_objs:
		serialized_data.append({
			'name': i.name,
			'value': i.value,
			'dimension': i.dimension,
			'modification': {
				'id': i.modification.id,
				'name': i.modification.name,
			}
		})
	return JsonResponse({ 'status': 'ok', 'properties': serialized_data })


@csrf_exempt
@require_POST
def api_add_properties(request):
	req = post_json(request)
	try:
		modification = req['modification']
		name = req['name']
		value = req['value']
		dimension = req['dimension']
		token = req['token']
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Name or modification id or value or dimension or token not passed', 'msg': 'Не переданы все параметры' })
	if not name or not token or not modification or not value or not dimension: return JsonResponse({ 'status': 'fail', 'reason': 'Empty some parameters',  'msg': 'Некоторые значения переданы пустые' })
	person = get_person_from_req(req)
	if not person: return JsonResponse({ 'status': 'fail', 'reason': 'No auth', 'msg': 'пользователь не авторизован' })
	try:
		modification = Modification.objects.get(id=modification)
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Modification not found', 'msg': 'Передано несуществующее значения id модификации' })
	obj = Property(modification=modification, name=name, value=value, dimension=dimension, is_visible=False)
	if person and person.is_admin: obj.is_visible = True
	obj.save()
	return JsonResponse({ 'status': 'ok', 'visible': obj.is_visible, 'id': obj.id })


@csrf_exempt
@require_POST
def api_get_table(request):
	req = post_json(request)
	table = []
	for element in Item.objects.filter(is_visible=True):
		table.append({
			'a': 'b'
		})
	return JsonResponse({ 'status': 'ok', 'table': table })


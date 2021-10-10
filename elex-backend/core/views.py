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
	except: return None


def debug(line):
	with open('./log', 'a') as f:
		f.write(line)


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
	if not person.is_active: return JsonResponse({ 'status': 'fail', 'reason': 'Not active person', 'msg': 'Пользователь неактивен' })
	return JsonResponse({ 'status': 'ok', 'name': person.name, 'isAdmin': person.is_admin, 'token': token })


@csrf_exempt
@require_POST
def api_token_info(request):
	req = post_json(request)
	try: token = req['token']
	except: return JsonResponse({ 'status': 'fail', 'reason': 'Token not passed', 'msg': 'Не передан токен'})
	person = get_person_from_req(req)
	if not person: return JsonResponse({ 'status': 'fail', 'reason': 'Invalid token', 'msg': 'Неверный токен' })
	if not person.is_active: return JsonResponse({ 'status': 'fail', 'reason': 'Not active person', 'msg': 'Пользователь неактивен' })
	return JsonResponse({ 'status': 'ok', 'name': person.name, 'isAdmin': person.is_admin, 'token': token })


@csrf_exempt
@require_POST
def api_token_delete(request):
	req = post_json(request)
	try: token = req['token']
	except: return JsonResponse({ 'status': 'fail', 'reason': 'Token not passed', 'msg': 'Не передан токен'})
	person = get_person_from_req(req)
	if not person: return JsonResponse({ 'status': 'fail', 'reason': 'Invalid token', 'msg': 'Неверный токен' })
	token = Token.objects.get(token=token)
	token.delete()
	return JsonResponse({ 'status': 'ok' })


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
def api_person_change_password(request):
	req = post_json(request)
	try:
		token = req['token']
		password = req['password']
	except:
		return JsonResponse({ 'status': 'fail', 'reason': 'Token or password not passed', 'msg': 'Не передано значения токена или пароля' })
	person = get_person_from_req(req)
	if not person or not person.is_active: return JsonResponse({ 'status': 'fail', 'reason': 'Invalid token', 'msg': 'Неверный токен' })
	if (len(password) == 0): return JsonResponse({ 'status': 'fail', 'reason': 'Empty password', 'msg': 'Передан пустой пароль' })
	person.password = make_password(password)
	person.save()
	# now delete all token except current token
	all_tokens = Token.objects.filter(person=person)
	for tokenObj in all_tokens:
		if tokenObj.token != token: token.delete()
	return JsonResponse({ 'status': 'ok' })


@csrf_exempt
@require_POST
def api_person_delete(request):
	req = post_json(request)
	try:
		token = req['token']
		user_id = req['user']
	except: JsonResponse({ 'status': 'fail', 'reason': 'Token or user not passed', 'msg': 'Не передано значение токена или пользователя' })
	person = get_person_from_req(req)
	if not person or not person.is_admin or person.id == user_id:
		return JsonResponse({ 'status': 'fail', 'reason': 'Not found admin or admin not admin or admin is user', 'msg': 'Выбрана некорректная пара пользователей' })
	try:
		user = Person.objects.get(id=user_id)
	except: JsonResponse({ 'status': 'fail', 'reason': 'User not found', 'msg': 'Нет пользователя, который соответствует указанному id' })
	user.delete()
	return JsonResponse({ 'status': 'ok' })


@csrf_exempt
@require_POST
def api_get_makers(request):
	req = post_json(request)
	person = get_person_from_req(req)
	if not person or not person.is_active: return JsonResponse({ 'status': 'fail', 'reason': 'Invalid token', 'msg': 'Неверный токен' })
	all_makers = []
	all_db_makers = Maker.objects.filter(is_visible=True)
	for i in all_db_makers:
		all_makers.append({
			'id': i.id,
			'name': i.name,
			'description': i.description,
		})
	return JsonResponse({ 'status': 'ok', 'objects': all_makers })


@csrf_exempt
@require_POST
def api_add_maker(request):
	req = post_json(request)
	person = get_person_from_req(req)
	if not person or not person.is_active: return JsonResponse({ 'status': 'fail' })
	try:
		name = req['name']
		description = req['description']
	except: return JsonResponse({ 'status': 'fail' })
	# validors
	if len(name) == 0 or len(description) == 0: return JsonResponse({ 'status': 'fail' })
	obj = Maker(name=name, description=description, is_visible = True if person.is_admin else False)
	obj.save()
	return JsonResponse({ 'status': 'ok', 'obj': { 'id': obj.id, 'name': obj.name, 'description': obj.description } if obj.is_visible else None })


@csrf_exempt
@require_POST
def api_get_types(request):
	req = post_json(request)
	person = get_person_from_req(req)
	if not person or not person.is_active: return JsonResponse({ 'status': 'fail', 'reason': 'Invalid token', 'msg': 'Неверный токен' })
	all_types = []
	all_db_types = Type.objects.filter(is_visible=True)
	for i in all_db_types:
		all_types.append({
			'id': i.id,
			'name': i.name,
			'description': i.description,
		})
	return JsonResponse({ 'status': 'ok', 'objects': all_types })


@csrf_exempt
@require_POST
def api_add_type(request):
	req = post_json(request)
	person = get_person_from_req(req)
	if not person or not person.is_active: return JsonResponse({ 'status': 'fail' })
	try:
		name = req['name']
		description = req['description']
	except: return JsonResponse({ 'status': 'fail' })
	# validors
	if len(name) == 0 or len(description) == 0: return JsonResponse({ 'status': 'fail' })
	obj = Type(name=name, description=description, is_visible = True if person.is_admin else False)
	obj.save()
	return JsonResponse({ 'status': 'ok', 'obj': { 'id': obj.id, 'name': obj.name, 'description': obj.description } if obj.is_visible else None })


@csrf_exempt
@require_POST
def api_get_elements(request):
	req = post_json(request)
	person = get_person_from_req(req)
	if not person or not person.is_active: return JsonResponse({ 'status': 'fail', 'reason': 'Invalid token', 'msg': 'Неверный токен' })
	all_elements = []
	all_db_elements = Item.objects.filter(is_visible=True)
	for i in all_db_elements:
		all_elements.append({
			'id': i.id,
			'maker': i.maker.id,
			'type': i.type.id,
			'name': i.name,
		})
	return JsonResponse({ 'status': 'ok', 'objects': all_elements })


@csrf_exempt
@require_POST
def api_add_element(request):
	req = post_json(request)
	person = get_person_from_req(req)
	if not person or not person.is_active: return JsonResponse({ 'status': 'fail' })
	try:
		name = req['name']
		_type = Type.objects.get(id=req['type'])
		maker = Maker.objects.get(id=req['maker'])
	except: return JsonResponse({ 'status': 'fail' })
	# validors
	if len(name) == 0: return JsonResponse({ 'status': 'fail' })
	obj = Item(maker=maker, type=_type, name=name, is_visible = True if person.is_admin else False)
	obj.save()
	return JsonResponse({ 'status': 'ok', 'obj': { 'id': obj.id, 'maker': obj.maker.id, 'type': obj.type.id, 'name': obj.name } if obj.is_visible else None })


@csrf_exempt
@require_POST
def api_get_modifications(request):
	req = post_json(request)
	person = get_person_from_req(req)
	if not person or not person.is_active: return JsonResponse({ 'status': 'fail', 'reason': 'Invalid token', 'msg': 'Неверный токен' })
	all_modifications = []
	all_db_modifications = Modification.objects.filter(is_visible=True)
	for i in all_db_modifications:
		all_modifications.append({
			'id': i.id,
			'item': i.item.id,
			'name': i.name,
		})
	return JsonResponse({ 'status': 'ok', 'objects': all_modifications })


@csrf_exempt
@require_POST
def api_add_modification(request):
	req = post_json(request)
	person = get_person_from_req(req)
	if not person or not person.is_active: return JsonResponse({ 'status': 'fail' })
	try:
		name = req['name']
		item = Item.objects.get(id=req['item'])
	except: return JsonResponse({ 'status': 'fail' })
	# validors
	if len(name) == 0: return JsonResponse({ 'status': 'fail' })
	obj = Modification(item=item, name=name, is_visible = True if person.is_admin else False)
	obj.save()
	return JsonResponse({ 'status': 'ok', 'obj': { 'id': obj.id, 'item': obj.item.id, 'name': obj.name } if obj.is_visible else None })


@csrf_exempt
@require_POST
def api_get_properties(request):
	req = post_json(request)
	person = get_person_from_req(req)
	if not person or not person.is_active: return JsonResponse({ 'status': 'fail', 'reason': 'Invalid token', 'msg': 'Неверный токен' })
	all_properties = []
	all_db_properties = Property.objects.filter(is_visible=True)
	for i in all_db_properties:
		all_properties.append({
			'id': i.id,
			'modification': i.modification.id,
			'name': i.name,
			'value': i.value,
			'dimension': i.dimension,
		})
	return JsonResponse({ 'status': 'ok', 'objects': all_properties })

# ============================= admin views ====================================


def admin_check(req):
	person = get_person_from_req(req)
	if not person or not person.is_active or not person.is_admin: return False
	return True


@csrf_exempt
@require_POST
def api_admin_get_users(request):
	req = post_json(request)
	if not admin_check(req): return JsonResponse({ 'status': 'fail', 'reason': 'User is not admin', 'msg': 'Пользователь не является администрацией' })
	users_serialized = [{
		'id': i.id, 'is_active': i.is_active, 'name': i.name, 'description': i.description, 'is_admin': i.is_admin
	} for i in Person.objects.all()]
	return JsonResponse({ 'status': 'ok', 'users': users_serialized })


@csrf_exempt
@require_POST
def api_admin_set_user(request):
	req = post_json(request)
	if not admin_check(req): return JsonResponse({ 'status': 'fail', 'reason': 'User is not admin', 'msg': 'Пользователь не является администрацией' })
	admin = get_person_from_req(req)
	if not req.__contains__('user'): return JsonResponse({ 'status': 'fail', 'reason': 'User not provided', 'msg': 'Не передан пользователь' })
	try: user = Person.objects.get(id=req['user'])
	except: return JsonResponse({ 'status': 'fail', 'reason': 'User not found', 'msg': 'Не найден пользователь с таким id' })

	available_fields = [
		{ 'name': 'is_admin',  'type': 'Boolean', 'can_change_self': False },
		{ 'name': 'is_active', 'type': 'Boolean', 'can_change_self': False },
	]

	for field in available_fields:
		if not req.__contains__(field['name']): continue
		if admin.id == user.id and not field['can_change_self']: return JsonResponse({ 'status': 'fail', 'reason': 'Not permitted change self account', 'msg': 'Запрещено менять свои поля' })
		setattr(user, field['name'], req[field['name']])

	user.save()

	return JsonResponse({ 'status': 'ok', 'user': { 'id': user.id, 'is_active': user.is_active, 'name': user.name, 'description': user.description, 'is_admin': user.is_admin } })


# ==============================================================================

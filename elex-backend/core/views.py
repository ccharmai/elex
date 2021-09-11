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
def api_get_makers(request):
	req = post_json(request)
	try: token = req['token']
	except: return JsonResponse({ 'status': 'fail', 'reason': 'Token not passed', 'msg': 'Не передан токен'})
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
def api_get_types(request):
	req = post_json(request)
	try: token = req['token']
	except: return JsonResponse({ 'status': 'fail', 'reason': 'Token not passed', 'msg': 'Не передан токен'})
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
def api_get_elements(request):
	req = post_json(request)
	try: token = req['token']
	except: return JsonResponse({ 'status': 'fail', 'reason': 'Token not passed', 'msg': 'Не передан токен'})
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
def api_get_modifications(request):
	req = post_json(request)
	try: token = req['token']
	except: return JsonResponse({ 'status': 'fail', 'reason': 'Token not passed', 'msg': 'Не передан токен'})
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

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
import json

from .auth import get_person_from_req, create_token
from .validators import validate_new_user
from .models import Person


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
	status = validate_new_user(name)
	if not status: return JsonResponse({ 'status': 'fail', 'reason': 'Name taken', 'msg': 'Имя пользователя занято' })
	Person(name=name, password=make_password(password)).save()
	status, token, person = create_token(name, password)
	return JsonResponse({ 'status': 'ok', 'name': person.name, 'isAdmin': person.is_admin, 'token': token })

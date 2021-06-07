from .models import Token, Person
from django.contrib.auth.hashers import check_password

from .generators import generate_token


def auth_person_from_token(token):
	try:
		obj = Token.objects.get(token=token, is_active=True)
		return obj.person
	except:
		return None


def get_person_from_req(req):
	try:
		token = req["token"]
		return auth_person_from_token(token)
	except:
		return None


def auth(name, password):
	try:
		person = Person.objects.get(name=name)
		if check_password(password, person.password):
			return person
		return None
	except:
		return None


def create_token(name, password):
	# return status, token, person

	person = auth(name, password)
	if not person: return False, '', None
	token = generate_token()
	Token(token=token, person=person).save()
	return True, token, person


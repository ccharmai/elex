import random, string
from .models import Token


def generate_token(size=50):
	tokens_obj = Token.objects.all()
	token_obj_uniq = [i.token for i in tokens_obj]
	while True:
		potential_token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))
		if potential_token not in token_obj_uniq:
			return potential_token

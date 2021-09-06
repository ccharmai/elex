from .models import Person

def validate_new_user(name):
	persons = Person.objects.all()
	used_names = [i.lower() for i in persons]
	if name.lower() not in used_names: return True
	return False

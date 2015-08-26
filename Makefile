test:
	cd src; coverage run --source='.' manage.py test; coverage report -m

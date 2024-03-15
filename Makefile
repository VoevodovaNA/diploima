mm:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

runserv:
	python3 manage.py runserver

run:
	mm migrate runserv
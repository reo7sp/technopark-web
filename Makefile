.PHONY: main run-nginx run-django browse install

main:


run-nginx:
	nginx -p . -c nginx.conf

run-django:
	gunicorn ask_morozenkov.wsgi

run-wsgi-test:
	gunicorn wsgi:wsgi_app


browse:
	open http://localhost:8080


install:
	pip install -r requirements.txt

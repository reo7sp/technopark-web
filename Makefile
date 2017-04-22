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


test-wsgi:
	curl -X GET "http://localhost:8000/wsgi-test/?a=b&c=d"; python -c 'print("-" * 80)'
	curl -X POST -d "a=b&c=d" http://localhost:8000/wsgi-test/


install:
	pip install -r requirements.txt

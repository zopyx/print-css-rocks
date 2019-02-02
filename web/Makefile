install:
	python3 -m venv .
	bin/pip install -r requirements.txt

serve:
	bin/gunicorn server:app --bind 0.0.0.0:8000 --worker-class sanic.worker.GunicornWorker

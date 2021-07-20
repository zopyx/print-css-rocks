install:
	python3 -m venv .
	bin/pip install -r requirements.txt

serve:
	LESSON_ROOT=../lessons bin/gunicorn server:app --bind 0.0.0.0:8000 --worker-class sanic.worker.GunicornWorker

serve-beta:
	LESSON_ROOT=../lessons bin/gunicorn server:app --bind 0.0.0.0:8001 --worker-class sanic.worker.GunicornWorker

install:
	python3 -m venv .
	bin/pip install -r requirements.txt

serve:
	LESSON_ROOT=../lessons bin/hypercorn server:app --bind 0.0.0.0:8000 --graceful-timeout 1

serve-beta:
	LESSON_ROOT=../lessons bin/hypercorn server:app --bind 0.0.0.0:8001 --graceful-timeout 1

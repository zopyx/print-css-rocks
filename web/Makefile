install:
	uv venv -p 3.13 
	uv pip install -r requirements.txt

serve:
	LESSON_ROOT=../lessons bin/hypercorn server:app --bind 0.0.0.0:8000 --graceful-timeout 1 --reload

serve-beta:
	LESSON_ROOT=../lessons bin/hypercorn server:app --bind 0.0.0.0:8001 --graceful-timeout 1

build: 
	docker build -t zopyx/print-css-rocks .

build-clean: 
	docker build --no-cache -t zopyx/print-css-rocks .

push:
	docker push zopyx/print-css-rocks


serve:
#	-docker pull zopyx/print-css-rocks
	-docker stop pp-server
	-docker kill pp-server
	-docker rm pp-server
	docker run --rm -ti -p 8000:8000 --security-opt seccomp=./chrome.json --name pp-server zopyx/print-css-rocks


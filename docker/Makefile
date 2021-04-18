TOPDIR=$(PWD)

build: 
	-cp /usr/local/AHFormatterV71/etc/AHFormatter.lic .
	-cp /usr/AHFormatterV71_64/etc/AHFormatter.lic .
#	-cp /Applications/PDFreactor/jetty/lib/ext/licensekey.txt .
	docker build -t zopyx/print-css-rocks . --build-arg TS_DOWNLOAD=${TS_DOWNLOAD} --build-arg AH_DOWNLOAD=${AH_DOWNLOAD}

build-clean: 
	docker build --no-cache -t zopyx/print-css-rocks .

push:
	docker push zopyx/print-css-rocks


serve:
#	-docker pull zopyx/print-css-rocks
	-docker stop pp-server
	-docker kill pp-server
	-docker rm pp-server
	docker run -p 8000:8000 --name pp-server zopyx/print-css-rocks

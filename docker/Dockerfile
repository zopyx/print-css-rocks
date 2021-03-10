FROM ubuntu:21.04
ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update; apt upgrade -y
RUN apt-get install -y build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

RUN apt-get install -y python3-dev python3-venv wget npm unzip
RUN python3 --version
RUN python3 -m venv /tmp/python
RUN /tmp/python/bin/pip3 install pp.server

RUN ls /tmp/python/bin
RUN /tmp/python/bin/pip3 install weasyprint


RUN wget -q -O prince.deb https://www.princexml.com/download/prince_14-1_ubuntu20.04_amd64.deb
RUN apt install -y ./prince.deb
RUN prince --version

RUN wget -q -O speedata.zip https://download.speedata.de/dl/speedata-publisher-linux-amd64-4.2.0.zip
RUN unzip speedata.zip

RUN npm install -g @vivliostyle/cli
RUN vivliostyle --version

RUN npm install -g pagedjs-cli
RUN pagedjs-cli --version

#RUN wget -q -O pdfreactor.tgz "https://www.pdfreactor.com/download/get/?product=pdfreactor&type=windows-x64_installer&jre=true&archive=true"
#RUN tar xfz pdfreactor.tgz
#RUN PDFreactor/bin/pdfreactorwebservice start

RUN prince --version
RUN vivliostyle --version
RUN pagedjs-cli --version
RUN /tmp/python/bin/weasyprint --version
RUN speedata-publisher/bin/sp --version

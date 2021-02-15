FROM ubuntu:latest
ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update; apt upgrade -y


RUN apt-get install -y python3-dev python3-venv wget npm
RUN python3 --version
RUN python3 -m venv /tmp/python

RUN ls /tmp/python/bin
RUN /tmp/python/bin/pip3 install weasyprint


RUN wget -O prince.deb https://www.princexml.com/download/prince_14-1_ubuntu20.04_amd64.deb
RUN apt install -y ./prince.deb
RUN prince --version

RUN apt install -y curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -yq nodejs build-essential

RUN node --version
RUN npm install  pagedjs-cli
RUN pagedjs-cli --version

FROM ubuntu:latest
LABEL maintainer="info@zopyx.com"

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update; apt upgrade -y; \
    apt-get install -y build-essential python3-dev python3-pip python3-setuptools \
        python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
        libgdk-pixbuf2.0-0 libffi-dev shared-mime-info python3-dev python3-venv \
        wget npm unzip curl tini; \
    apt-get clean

ADD chromium.pref /etc/apt/preferences.d/chromium.pref
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium

RUN echo "deb http://deb.debian.org/debian buster main" >> /etc/apt/sources.list.d/debian.list && \
 echo "deb http://deb.debian.org/debian buster-updates main" >> /etc/apt/sources.list.d/debian.list && \
 echo "deb http://deb.debian.org/debian-security buster/updates main" >> /etc/apt/sources.list.d/debian.list && \
 apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DCC9EFBF77E11517 && \
 apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 648ACFD622F3D138 && \
 apt-key adv --keyserver keyserver.ubuntu.com --recv-keys AA8E81B4331F7F50 && \
 apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 112695A0E562B32A && \
 apt update && \
 apt install chromium -y && \
 apt-get clean && rm -rf /var/cache/apk/*

RUN python3 -m venv /tmp/python
RUN /tmp/python/bin/pip3 install --no-cache wheel pp.server hypercorn weasyprint

RUN wget -q -O prince.deb https://www.princexml.com/download/prince_14.2-1_ubuntu20.04_amd64.deb; \
    apt install -y ./prince.deb; \
    rm prince.deb
RUN wget -q -O speedata.zip https://download.speedata.de/dl/speedata-publisher-linux-amd64-4.5.10.zip; \
    unzip speedata.zip; \
    rm speedata.zip


RUN export PUPPETEER_SKIP_DOWNLOAD='true' && npm install   pagedjs-cli
RUN export PUPPETEER_SKIP_DOWNLOAD='true' && npm install   @vivliostyle/cli

# Set user and group
ARG user=appuser
ARG group=appuser
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} -s /bin/sh -m ${user} # <--- the '-m' create a user home directory

ADD start-server.sh /
RUN chmod a+rx /start-server.sh

USER ${uid}:${gid}
EXPOSE 8000/tcp
ENTRYPOINT ["tini", "-p", "SIGKILL", "-v", "--", "/start-server.sh"]

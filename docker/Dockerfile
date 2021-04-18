FROM ubuntu:latest
LABEL maintainer="info@zopyx.com"

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update; apt upgrade -y; \
    apt-get install -y build-essential python3-dev python3-pip python3-setuptools \
        python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
        libgdk-pixbuf2.0-0 libffi-dev shared-mime-info python3-dev python3-venv \
        default-jre php alien rpl wget npm unzip curl tini; \
    apt-get clean

RUN python3 -m venv /tmp/python
RUN /tmp/python/bin/pip3 install wheel pp.server hypercorn weasyprint

RUN wget -q -O prince.deb https://www.princexml.com/download/prince_14-1_ubuntu20.04_amd64.deb; \
    apt install -y ./prince.deb; \
    rm prince.deb
RUN wget -q -O speedata.zip https://download.speedata.de/dl/speedata-publisher-linux-amd64-4.2.0.zip; \
    unzip -q speedata.zip; \
    rm speedata.zip

RUN export PUPPETEER_SKIP_DOWNLOAD='true' && npm install   pagedjs-cli
RUN export PUPPETEER_SKIP_DOWNLOAD='true' && npm install   @vivliostyle/cli


#RUN PDFreactor/bin/pdfreactorwebservice start

# Antennahouse
ARG AH_DOWNLOAD
ENV AH_DOWNLOAD=$AH_DOWNLOAD
RUN wget -q -O ah.rpm.gz ${AH_DOWNLOAD} ; \
        gzip -d ah.rpm; \
        alien -i ah.rpm; \
        rm ah.rpm; \
        rpl '@@HOME@@' '/usr/AHFormatterV71_64' /usr/AHFormatterV71_64/run.sh
COPY AHFormatter.lic /usr/AHFormatterV71_64/etc/AHFormatter.lic

# Typeset.sh
ARG TS_DOWNLOAD
ENV TS_DOWNLOAD=$TS_DOWNLOAD
RUN echo $TS_DOWNLOAD
RUN wget -q -O /usr/bin/typeset.sh.phar ${TS_DOWNLOAD} ; \
    chmod +x /usr/bin/typeset.sh.phar; 

# Calibre
RUN wget -q -nv -O- https://download.calibre-ebook.com/linux-installer.sh | bash /dev/stdin

RUN cat /etc/os-release
RUN apt install -y default-jre
RUN java --version


RUN wget -q -O pdfreactor.zip "https://www.pdfreactor.com/download/get/?product=pdfreactor&type=windows-x64_installer&jre=true&archive=true"
RUN unzip pdfreactor.zip
RUN find . -name pdfreactor.jar

ADD pdfreactor.sh /
ADD test.html /
ADD licensekey.txt /
ADD start-server.sh /
RUN chmod a+rx /start-server.sh /pdfreactor.sh
#RUN /pdfreactor.sh file:///test.html out.pdf

RUN mkdir /data
EXPOSE 8000/tcp
ENTRYPOINT ["tini", "-p", "SIGKILL", "-v", "--", "/start-server.sh"]

FROM ubuntu:latest
LABEL maintainer="info@zopyx.com"

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update; apt upgrade -y; \
    apt-get install -y build-essential python3-dev python3-pip python3-setuptools \
        python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
        libgdk-pixbuf2.0-0 libffi-dev shared-mime-info python3-dev python3-venv \
        php alien rpl wget npm unzip curl tini; \
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


#RUN wget -q -O pdfreactor.tgz "https://www.pdfreactor.com/download/get/?product=pdfreactor&type=windows-x64_installer&jre=true&archive=true"
#RUN tar xfz pdfreactor.tgz
#RUN PDFreactor/bin/pdfreactorwebservice start

RUN wget -q -O ah.rpm.gz "https://www.antenna.co.jp/xml/download/ahf71-69f6cc18-0cc2-43fb-aa37-05caa420802d/R1/AHFormatterV71_64-7.1E-R1.x86_64.rpm.gz" ; \
        gzip -d ah.rpm; \
        alien -i ah.rpm; \
        rm ah.rpm.gz; \
        rpl '@@HOME@@' '/usr/AHFormatterV71_64' /usr/AHFormatterV71_64/run.sh

RUN wget -q -O /usr/bin/typeset.sh.phar http://typeset.sh/phar/demo/jung-Zt5gSfTm5Eyt8x08ducHR \;
    chmod +x /usr/bin/typeset.sh.phar; \

ADD start-server.sh /
RUN chmod a+rx /start-server.sh
EXPOSE 8000/tcp
ENTRYPOINT ["tini", "-p", "SIGKILL", "-v", "--", "/start-server.sh"]

#!/bin/bash

export PATH=$PATH:\
/:\
/tmp/python/bin:\
/speedata-publisher/bin:\
/node_modules/.bin:\
/usr/AHFormatterV71_64:\
/PDFreactor/clients/cli\

chmod a+rx /PDFreactor/clients/cli/pdfreactor.py

/PDFreactor/bin/pdfreactorwebservice start

/tmp/python/bin/pip3 install --pre -U pp.server

hypercorn pp.server.server:app --bind 0.0.0.0:8000 --access-logfile /data/access.log --error-logfile /data/error.log --workers 1


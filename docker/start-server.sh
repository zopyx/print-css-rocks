#!/bin/bash

export PATH=$PATH:\
/:\
/tmp/python/bin:\
/speedata-publisher/bin:\
/node_modules/.bin:\
/usr/AHFormatterV71_64:\
/app/PDFreactor/clients/cli

chmod a+rx /app/PDFreactor/clients/cli/pdfreactor.py
ls -la  /app/PDFreactor/clients/cli/pdfreactor.py

/tmp/python/bin/pip3 install -U pp.server

hypercorn pp.server.server:app --bind 0.0.0.0:8000 --access-logfile /data/access.log --error-logfile /data/error.log --workers 1


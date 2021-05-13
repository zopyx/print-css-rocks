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

export PP_SPOOL_DIRECTORY=/tmp

hypercorn pp.server.server:app --bind 0.0.0.0:8000 --access-logfile /tmp/access.log --error-logfile /tmp/error.log --workers 1


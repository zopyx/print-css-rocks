#!/bin/bash

export PATH=$PATH:\
/:\
/tmp/python/bin:\
/speedata-publisher/bin:\
/node_modules/.bin:\
/usr/AHFormatterV71_64

hypercorn pp.server.server:app --bind 0.0.0.0:8000 --access-logfile /data/access.log --error-logfile /data/error.log --workers 1


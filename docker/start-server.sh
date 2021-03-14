#!/bin/bash

export PATH=$PATH:\
/:\
/tmp/python/bin:\
/speedata-publisher/bin:\
/node_modules/.bin

hypercorn pp.server.server:app --bind 0.0.0.0:8000


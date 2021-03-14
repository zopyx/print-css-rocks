#!/bin/bash

export PATH=$PATH:\
/:\
/tmp/python/bin:\
/speedata-publisher/bin:\
/node_modules/.bin

sp --version
weasyprint --version
pagedjs-cli --version
prince --version
vivliostyle --version

hypercorn pp.server.server:app --bind 0.0.0.0:8000


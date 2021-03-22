#!/bin/bash

ls -la /PDFreactor/lib
java -Dcom.realobjects.pdfreactor.webservice.licenseKeyUrl=file:///licensekey.txt  -jar /PDFreactor/lib/pdfreactor.jar  -i $1 -o $2

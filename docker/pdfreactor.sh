#!/bin/bash

ls -la /PDFreactor/lib
java -jar /PDFreactor/lib/pdfreactor.jar -i $1 -o $2

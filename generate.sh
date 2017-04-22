#!/bin/bash

set -x
target=$PWD/docs/source/generated

git rm -fr $target
rm -fr $target
mkdir -p $target

for d in lesson-*
do
	echo $d
    mkdir -p $target/$d
    cd $d 
    make 
    make images
    cp -a *pdf $target/$d
    cp -a images $target/$d
    cd ..
done

git add $target

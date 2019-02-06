#!/bin/bash

set -x
generated_dir=$PWD/generated

git rm -fr $generated_dir
rm -fr $generated_dir
mkdir -p $generated_dir

for d in lesson-*
do
    echo "*******************************************************************"
	echo $d
    mkdir -p $generated_dir/$d
    cd $d 
    make 
    make images
    cp -a *pdf $generated_dir/$d
    cp -a images $generated_dir/$d
    cd ..
done

git add $generated_dir

#!/bin/bash

while read line
do
    dirname=`echo $line | cut -d "|" -f1`
    url=`echo $line | cut -d "|" -f2`
    mkdir -p "$dirname"
    pushd "$dirname"
    wget $url
    popd
done < urls.txt

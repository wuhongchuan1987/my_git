#!/bin/bash

path=`pwd`
dir_name=`basename $path`
tmp_name=`echo $dir_name`
file_name=`basename $path/$tmp_name*py`
for i in `ps -ef | grep $file_name | grep -v grep | awk '{print $2}'`;do
kill $i;done

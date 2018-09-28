#!/bin/bash

path=`pwd`
dir_name=`basename $path`
tmp_name=`echo $dir_name`
abs_name=`ls $path/$tmp_name*py`
nohup /usr/bin/python $abs_name > /dev/null 2>&1

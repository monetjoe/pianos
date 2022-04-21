#! /bin/bash

cat search/search-01.csv | awk -F ',' '{print $1 $4 $14}' | sed -n '3,20p'

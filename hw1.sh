#!/bin/bash

read input < input.txt

ping -c3 $input >> output.log
ping -c3 google.com >> output.log


echo "The value of \$input = $input"

echo $(date) >> output.log 

echo >> output.log

echo "done"

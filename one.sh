#!/bin/bash

for py_file in $(find ../one -name '*.py')
do
    python3 $py_file
done

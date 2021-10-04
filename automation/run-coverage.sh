#!/bin/bash

export PYTHONPATH="$(pwd)/lab_1:$(pwd)/lab_2:$(pwd)/lab_3:$(pwd)/lab_4:$(pwd):${PYTHONPATH}"
coverage run -m unittest discover -p "*_test.py"
coverage report -m
coverage xml
coverage-lcov

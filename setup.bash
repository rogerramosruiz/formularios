#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    py_comand=python3
elif [[ "$OSTYPE" == "msys" ]]; then
    py_comand=python
elif [[ "$OSTYPE" == "win32" ]]; then
    py_comand=python
fi


$py_comand manage.py migrate
$py_comand manage.py loaddata fixtures/*
$py_comand user_creation.py
$py_comand manage.py createsuperuser
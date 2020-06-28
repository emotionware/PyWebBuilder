#!/bin/bash
cd /var/www/4tproccess
virtualenv /var/www/4tproccess/4tpyenv
source /var/www/4tproccess/4tpyenv/bin/activate
python3 runserver.py

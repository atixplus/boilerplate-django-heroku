#!/bin/bash

cd backend/webapp

./manage.py collectstatic --no-input
./manage.py migrate --no-input
#./manage.py loaddata ../demo/demo.json
